import pkg_resources


def read_resource(relative_path):
    absolute_path = pkg_resources.resource_filename('chordchart_notation',
                                                    relative_path)

    with open(absolute_path, 'r') as fd:
        content = fd.read()

    return content


template = read_resource('render/html_template.html')
style = read_resource('render/html_style.css')


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
        self._label = None
        self._lines = []
        self._new_line()

    def _last_line(self):
        return self._lines[-1]

    def get_result(self):
        result = ''

        for line in self._lines:
            result += line.get_result()

        return result

    def label(self, value):
        self._last_line().label(value)

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
        self._label = ''

    def get_result(self):
        label = ''
        mark_line = ''
        alt_line = ''
        base_line = ''

        if self._label:
            label = f'<tr><td class="label"><span>{self._label}</span></td></tr>'

        for element in self._elements:
            alt_line += element.get_alt_line()
            mark_line += element.get_mark_line()
            base_line += element.get_base_line()

        lines = [
            label,
            f'<tr class="marks">{mark_line}</tr>',
            f'<tr class="alts">{alt_line}</tr>',
            f'<tr class="base">{base_line}</tr>'
        ]

        return '\n'.join(lines)

    def label(self, value):
        self._label = value

    def barline(self):
        builder = BarlineBuilder()
        self._previous_barline = builder
        self._elements.append(builder)
        return builder

    def measure(self):
        builder = MeasureBuilder(self._previous_barline)
        self._elements.append(builder)
        return builder


class BarlineBuilder:

    def __init__(self):
        self._mark = MarkBuilder()
        self._symbol = None
        self._alt = AlternativeBuilder()
        self._has_alt = False

    def __enter__(self):
        return self

    def __exit__(self, *args, **kwargs):
        pass

    def get_alt_line(self):
        if self._has_alt:
            return self._alt.get_result(1)
        return ''

    def get_mark_line(self):
        rowspan = None if self._has_alt else 2
        return self._mark.get_result(rowspan=rowspan)

    def get_base_line(self):
        if self._symbol:
            return f'<td class="barline">{self._symbol}</td>'

        return ''

    def alternative(self):
        self._has_alt = True
        return self._alt

    def build_initial_barline(self):
        # 𝄃
        self._symbol = '''
            <svg xmlns="http://www.w3.org/2000/svg" viewbox="0 0 100 300">
                <rect x="41" width="18" height="300"/>
                <rect x="69" width="3" height="300"/>
            </svg>
        '''

    def build_final_barline(self):
        # 𝄂
        self._symbol = '''
            <svg xmlns="http://www.w3.org/2000/svg" viewbox="0 0 100 300">
                <rect x="28" width="3" height="300"/>
                <rect x="41" width="18" height="300"/>
            </svg>
        '''

    def build_initial_repeat_barline(self):
        # 𝄆
        self._symbol = '''
            <svg xmlns="http://www.w3.org/2000/svg" viewbox="0 0 100 300">
                <rect x="41" width="18" height="300"/>
                <rect x="69" width="3" height="300"/>
                <circle cx="90" cy="120" r="9"/>
                <circle cx="90" cy="180" r="9"/>
            </svg>
        '''

    def build_final_repeat_barline(self):
        # 𝄇
        self._symbol = '''
            <svg xmlns="http://www.w3.org/2000/svg" viewbox="0 0 100 300">
                <circle cx="10" cy="120" r="9"/>
                <circle cx="10" cy="180" r="9"/>
                <rect x="28" width="3" height="300"/>
                <rect x="41" width="18" height="300"/>
            </svg>
        '''

    def build_single_barline(self):
        # 𝄀
        self._symbol = '''
            <svg xmlns="http://www.w3.org/2000/svg" viewbox="0 0 100 300">
                <rect x="47" width="6" height="300"/>
            </svg>
        '''

    def build_double_barline(self):
        # 𝄁
        self._symbol = '''
            <svg xmlns="http://www.w3.org/2000/svg" viewbox="0 0 100 300">
                <rect x="41" width="6" height="300"/>
                <rect x="53" width="6" height="300"/>
            </svg>
        '''

    def build_repeat_barline(self):
        # 𝄆
        self._symbol = '''
            <svg xmlns="http://www.w3.org/2000/svg" viewbox="0 0 100 300">
                <rect x="41" width="18" height="300"/>
                <rect x="69" width="3" height="300"/>
                <circle cx="90" cy="120" r="9"/>
                <circle cx="90" cy="180" r="9"/>
            </svg>
        '''

    def build_end_repeat_barline(self):
        # 𝄇
        self._symbol = '''
            <svg xmlns="http://www.w3.org/2000/svg" viewbox="0 0 100 300">
                <circle cx="10" cy="120" r="9"/>
                <circle cx="10" cy="180" r="9"/>
                <rect x="28" width="3" height="300"/>
                <rect x="41" width="18" height="300"/>
            </svg>
        '''

    def build_mark(self):
        self._mark = MarkBuilder()
        return self._mark


class MarkBuilder:

    def __init__(self):
        self._classes = ['mark']
        self._value = ''

    def get_result(self, span=None, rowspan=None):
        result = '<td'

        if span:
            result += f' colspan="{span}"'

        if rowspan:
            result += f' rowspan="{rowspan}"'

        if self._value and self._classes:
            result += f' class="{" ".join(self._classes)}"'

        result += '>'
        result += self._value
        result += '</td>'

        return result

    def build_segno_symbol(self):
        self._classes.append('segno')
        self._value = '𝄋'


class MeasureBuilder:

    def __init__(self, previous_barline):
        self._previous_barline = previous_barline
        self._elements = []
        self._alt = None

    def __enter__(self):
        return self

    def __exit__(self, *args, **kwargs):
        self._span = int(4 / len(self._elements))

    def get_alt_line(self):
        return ''

    def get_mark_line(self):
        rowspan = None if self._alt else 2
        return '\n'.join([element.get_mark_line(self._span, rowspan)
                          for element in self._elements])

    def get_base_line(self):
        return '\n'.join([element.get_base_line(self._span)
                          for element in self._elements])

    def chord(self):
        if self._alt:
            self._alt.extend()
        builder = ChordBuilder()
        self._elements.append(builder)
        return builder

    def chord_continuation(self):
        if self._alt:
            self._alt.extend()
        builder = ChordContinuationBuilder()
        self._elements.append(builder)
        return builder

    def alternative(self):
        self._alt = self._previous_barline.alternative()
        return self._alt


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
        span = int(4 / self._measure_length)

        number = f'<span class="number">{self._value}</span>' if self._value \
            else ''

        result = f'<td class="alternative">{number}</td>'
        result += f'<td colspan="{span}"></td>' * self._measure_length

        return result

    def build_number(self, value):
        self._value = f'{value}.'


class AlternativeTailBuilder:

    def __init__(self):
        self._measure_length = 0
        self._active = False


class ChordContinuationBuilder:

    def __init__(self):
        self._mark = MarkBuilder()

    def __enter__(self):
        return self

    def __exit__(self, *args, **kwargs):
        pass

    def get_mark_line(self, span, rowspan):
        return self._mark.get_result(span, rowspan)

    def get_base_line(self, span):
        colspan = f' colspan="{span}"' if span else ''
        result = f'<td class="chord-continuation"{colspan}>'
        result += '/</td>'

        return result


class ChordBuilder:

    def __init__(self):
        self._mark = MarkBuilder()
        self._kind = ChordKindBuilder()
        self._bass = ChordBassBuilder()

    def __enter__(self):
        return self

    def __exit__(self, *args, **kwargs):
        pass

    def get_mark_line(self, span, rowspan):
        return self._mark.get_result(span, rowspan)

    def get_base_line(self, span):
        colspan = f' colspan="{span}"' if span else ''
        result = f'<td class="chord"{colspan}>'
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
