style = '''
.chordchart {
    width: 80em;
    margin: auto;
}
.chordchart > * {
    margin: auto;
}
.chordchart .title {
    text-align: center;
    padding: .2em .8em;
}
.chordchart .composer {
    text-align: right;
    padding: .2em .8em;
}
.chordchart table {
    font-size: 2em;
    width: 100%;
}
.chordchart .barline {
    font-size: 2em;
    text-align: right;
}
.chordchart :first-child.barline {
    text-align: left;
}
.chordchart .chord {
    padding: 0 .5em;
}
.chordchart .chord-continuation {
    font-size: 1.5em;
    padding: 0 .5em;
}
.segno {
    font-size: 1.5em;
}
.alternative {
    font-size: .6em;
    border-top: solid 1px black;
    border-left: solid 2px black;
}
.alternative > * {
    padding: .3em;
}
'''

template = '''
<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8" />
        <meta name="viewport" content="width=device-width" />
        <title>{head_title}</title>
        <style>{style}</style>
    </head>
    <body>
        <div class="chordchart">
            <h1 class="title">{title}</h1>
            <h2 class="composer">{composer}</h2>
            <table class="chordchart">
                {parts}
            </table>
        </section>
    </body>
</html>
'''


class HtmlBuilder:

    def __init__(self):
        self._title = None
        self._composer = None
        self._parts = []

    def get_result(self):
        return template.format(
            title=self._title,
            composer=self._composer,
            head_title=self._head_title,
            style=style,
            parts='\n'.join([part.get_result()
                             for part in self._parts])
        )

    @property
    def _head_title(self):
        if self._composer:
            return f'{self._title} — {self._composer}'

        return self._title

    def set_title(self, value):
        self._title = value

    def set_composer(self, value):
        self._composer = value

    def part(self):
        builder = PartBuilder()
        self._parts.append(builder)
        return builder


class PartBuilder:

    def __init__(self):
        self._lines = []
        self._new_line()

    def _last_line(self):
        return self._lines[-1]

    def get_result(self):
        result = ''

        for line in self._lines:
            result += line.get_result()

        return result

    def barline(self):
        self._barline = self._last_line().barline()
        return self._barline

    def measure(self):
        return self._last_line().measure()

    def _new_line(self):
        self._lines.append(PartLine())

    def new_line(self):
        self._new_line()

        with self.barline() as barline:
            barline.build_single_barline()


class PartLine:

    def __init__(self):
        self._elements = []

    def get_result(self):
        alt_line = ''
        mark_line = ''
        base_line = ''

        for element in self._elements:
            alt_line += element.get_alt_line()
            mark_line += element.get_mark_line()
            base_line += element.get_base_line()

        lines = [
            f'<tr>{mark_line}</tr>',
            f'<tr>{alt_line}</tr>',
            f'<tr>{base_line}</tr>'
        ]

        return '\n'.join(lines)

    def barline(self):
        builder = BarlineBuilder()
        self._elements.append(builder)
        return builder

    def measure(self):
        builder = MeasureBuilder()
        self._elements.append(builder)
        return builder


class BarlineBuilder:

    def __init__(self):
        self._mark = Spacer()
        self._symbol = None
        self._has_mark = False

    def __enter__(self):
        return self

    def __exit__(self, *args, **kwargs):
        pass

    def get_alt_line(self):
        return ''

    def get_mark_line(self):
        return self._mark.get_result()

    def get_base_line(self):
        if self._symbol:
            return f'<td class="barline">{self._symbol}</td>'

        return ''

    def build_initial_barline(self):
        self._symbol = '𝄃'

    def build_final_barline(self):
        self._symbol = '𝄂'

    def build_initial_repeat_barline(self):
        self._symbol = '𝄆'

    def build_final_repeat_barline(self):
        self._symbol = '𝄇'

    def build_single_barline(self):
        self._symbol = '𝄀'

    def build_double_barline(self):
        self._symbol = '𝄁'

    def build_repeat_barline(self):
        self._symbol = '𝄆'

    def build_end_repeat_barline(self):
        self._symbol = '𝄇'

    def build_mark(self):
        self._mark = MarkBuilder()
        return self._mark


class Spacer:

    def get_result(self, span=None):
        if span:
            return f'<td colspan="{span}"></td>'
        return f'<td></td>'


class MarkBuilder:

    def __init__(self):
        self._class = None

    def get_result(self, span=None):
        result = '<td'

        if span:
            result += f' colspan="{span}"'

        if self._class:
            result += f' class="{self._class}"'

        result += '>'
        result += self._value
        result += '</td>'

        return result

    def build_segno_symbol(self):
        self._class = 'segno'
        self._value = '𝄋'


class MeasureBuilder:

    def __init__(self):
        self._elements = []
        self._alt = AlternativeBuilder()

    def __enter__(self):
        return self

    def __exit__(self, *args, **kwargs):
        self._span = int(4 / len(self._elements))

    def get_alt_line(self):
        return self._alt.get_result(self._span)

    def get_mark_line(self):
        return '\n'.join([element.get_mark_line(self._span)
                          for element in self._elements])

    def get_base_line(self):
        return '\n'.join([element.get_base_line(self._span)
                          for element in self._elements])

    def chord(self):
        self._alt.extend()
        builder = ChordBuilder()
        self._elements.append(builder)
        return builder

    def chord_continuation(self):
        self._alt.extend()
        builder = ChordContinuationBuilder()
        self._elements.append(builder)
        return builder

    def alternative(self):
        builder = AlternativeBuilder()
        self._alt = builder
        return builder


class AlternativeBuilder:

    def __init__(self):
        self._value = None
        self._measure_length = 0

    def __enter__(self):
        return self

    def __exit__(self, *args, **kwargs):
        pass

    def extend(self):
        self._measure_length += 1

    def get_result(self, span):
        span = (self._measure_length * span) + 1

        if self._value:
            return (f'<td colspan="{span}" class="alternative">'
                    f'<span>{self._value}</span>'
                    '</td>')

        return ''

    def build_number(self, value):
        self._value = f'{value}.'


class ChordContinuationBuilder:

    def __init__(self):
        self._mark = Spacer()
        self._has_mark = False

    def __enter__(self):
        return self

    def __exit__(self, *args, **kwargs):
        pass

    def get_mark_line(self, span):
        return self._mark.get_result(span)

    def get_base_line(self, span):
        result = f'<td class="chord-continuation" colspan="{span}">'
        result += '𝄍</td>'

        return result


class ChordBuilder:

    def __init__(self):
        self._mark = Spacer()
        self._kind = ChordKindBuilder()
        self._bass = ChordBassBuilder()

    def __enter__(self):
        return self

    def __exit__(self, *args, **kwargs):
        pass

    def get_mark_line(self, span):
        return self._mark.get_result(span)

    def get_base_line(self, span):
        result = f'<td class="chord" colspan="{span}">'
        result += self._root.get_result()
        result += self._kind.get_result()
        result += self._bass.get_result()
        result += '</td>'

        return result

    def chord_root(self):
        self._root = ChordRootBuilder()
        return self._root

    def chord_kind(self):
        self._kind = ChordKindBuilder()
        return self._kind

    def chord_bass(self):
        self._bass = ChordBassBuilder()
        return self._bass

    def mark(self):
        self._mark = MarkBuilder()
        return self._mark


class ChordRootBuilder:

    def get_result(self):
        return self._note

    def build_note(self, value):
        self._note = value[0].upper()

        if len(value) == 2:
            self._note += '<sup>'
            self._note += value[1]
            self._note += '</sup>'


class ChordBassBuilder:

    def __init__(self):
        self._note = ''

    def get_result(self):
        if self._note:
            return f'<sub>/{self._note}</sub>'
        return self._note

    def build_note(self, value):
        self._note = value[0].upper()

        if len(value) == 2:
            self._note += '<sup>'
            self._note += value[1]
            self._note += '</sup>'


class ChordKindBuilder:

    def __init__(self):
        self._kind = ''

    def get_result(self):
        return self._kind

    def build_minor_sixth(self):
        self._kind = '<sup>m6</sup>'

    def build_minor_seventh(self):
        self._kind = '<sup>m7</sup>'

    def build_minor_nineth(self):
        self._kind = '<sup>m9</sup>'

    def build_minor_eleventh(self):
        self._kind = '<sup>m11</sup>'

    def build_minor_thirteenth(self):
        self._kind = '<sup>m13</sup>'

    def build_suspended_second(self):
        self._kind = '<sup>sus2</sup>'

    def build_suspended_fourth(self):
        self._kind = '<sup>sus4</sup>'

    def build_minor(self):
        self._kind = '<sup>m</sup>'

    def build_sixth(self):
        self._kind = '<sup>6</sup>'

    def build_major_seventh(self):
        self._kind = '<sup>M7</sup>'

    def build_seventh(self):
        self._kind = '<sup>7</sup>'

    def build_nineth(self):
        self._kind = '<sup>9</sup>'

    def build_eleventh(self):
        self._kind = '<sup>11</sup>'

    def build_thirteenth(self):
        self._kind = '<sup>13</sup>'

    def build_half_diminished(self):
        self._kind = '<sup>ø</sup>'

    def build_diminished(self):
        self._kind = '°'

    def build_augmented(self):
        self._kind = '+'
