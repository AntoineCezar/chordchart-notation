from .visitor import Visitor


class ChordchartDirector(Visitor):

    def __init__(self, builder):
        self._builder = builder
        self._visit___root__ = self._pass_thru
        self._visit_chordchart = self._pass_thru
        self._visit_body = self._pass_thru
        self._visit_header = self._pass_thru

    def _visit_title(self, node):
        self._builder.set_title(node.value)

    def _visit_composer(self, node):
        self._builder.set_composer(node.value)

    def _visit_part(self, node):
        builder = self._builder.part()
        visitor = PartDirector(builder)
        node.accept(visitor)


class PartDirector(Visitor):

    def __init__(self, builder):
        self._builder = builder
        self._measure_count = 0

    def _visit_label(self, node):
        self._builder.label(node.value)

    def _visit_barline(self, node):
        with self._builder.barline() as builder:
            visitor = BarlineDirector(builder)
            node.accept(visitor)

    def _visit_measure(self, node):
        if self._measure_count == 4:
            self._builder.new_line()
            self._measure_count = 0

        with self._builder.measure() as builder:
            visitor = MeasureDirector(builder)
            node.accept(visitor)

        self._measure_count += 1


class BarlineDirector(Visitor):

    def __init__(self, builder):
        self._builder = builder
        self._visit_type = self._pass_thru

    def _visit_initial_barline(self, node):
        self._builder.build_initial_barline()

    def _visit_final_barline(self, node):
        self._builder.build_final_barline()

    def _visit_initial_repeat_barline(self, node):
        self._builder.build_initial_repeat_barline()

    def _visit_final_repeat_barline(self, node):
        self._builder.build_final_repeat_barline()

    def _visit_single_barline(self, node):
        self._builder.build_single_barline()

    def _visit_double_barline(self, node):
        self._builder.build_double_barline()

    def _visit_repeat_barline(self, node):
        self._builder.build_repeat_barline()

    def _visit_end_repeat_barline(self, node):
        self._builder.build_end_repeat_barline()

    def _visit_mark(self, node):
        builder = self._builder.build_mark()
        visitor = MarkDirector(builder)
        node.accept(visitor)


class MarkDirector(Visitor):

    def __init__(self, builder):
        self._builder = builder

    def _visit_segno_symbol(self, node):
        self._builder.build_segno_symbol()


class MeasureDirector(Visitor):

    def __init__(self, builder):
        self._builder = builder

    def _visit_chord(self, node):
        with self._builder.chord() as builder:
            visitor = ChordDirector(builder)
            node.accept(visitor)

    def _visit_chord_continuation(self, node):
        with self._builder.chord_continuation() as builder:
            pass

    def _visit_alternative(self, node):
        with self._builder.alternative() as builder:
            visitor = AlternativeDirector(builder)
            node.accept(visitor)


class AlternativeDirector(Visitor):

    def __init__(self, builder):
        self._builder = builder

    def _visit_number(self, node):
        self._builder.build_number(node.value)


class ChordDirector(Visitor):

    def __init__(self, builder):
        self._builder = builder

    def _visit_root(self, node):
        builder = self._builder.chord_root()
        visitor = ChordRootDirector(builder)
        node.accept(visitor)

    def _visit_kind(self, node):
        builder = self._builder.chord_kind()
        visitor = ChordKindDirector(builder)
        node.accept(visitor)

    def _visit_bass(self, node):
        builder = self._builder.chord_bass()
        visitor = ChordBassDirector(builder)
        node.accept(visitor)


class ChordRootDirector(Visitor):

    def __init__(self, builder):
        self._builder = builder

    def _visit_note(self, node):
        self._builder.build_note(node.value)


class ChordBassDirector(Visitor):

    def __init__(self, builder):
        self._builder = builder

    def _visit_note(self, node):
        self._builder.build_note(node.value)


class ChordKindDirector(Visitor):

    def __init__(self, builder):
        self._builder = builder

    def _visit_minor_sixth(self, node):
        self._builder.build_minor_sixth()

    def _visit_minor_seventh(self, node):
        self._builder.build_minor_seventh()

    def _visit_minor_nineth(self, node):
        self._builder.build_minor_nineth()

    def _visit_minor_eleventh(self, node):
        self._builder.build_minor_eleventh()

    def _visit_minor_thirteenth(self, node):
        self._builder.build_minor_thirteenth()

    def _visit_suspended_second(self, node):
        self._builder.build_suspended_second()

    def _visit_suspended_fourth(self, node):
        self._builder.build_suspended_fourth()

    def _visit_minor(self, node):
        self._builder.build_minor()

    def _visit_sixth(self, node):
        self._builder.build_sixth()

    def _visit_major_seventh(self, node):
        self._builder.build_major_seventh()

    def _visit_seventh(self, node):
        self._builder.build_seventh()

    def _visit_nineth(self, node):
        self._builder.build_nineth()

    def _visit_eleventh(self, node):
        self._builder.build_eleventh()

    def _visit_thirteenth(self, node):
        self._builder.build_thirteenth()

    def _visit_half_diminished(self, node):
        self._builder.build_half_diminished()

    def _visit_diminished(self, node):
        self._builder.build_diminished()

    def _visit_augmented(self, node):
        self._builder.build_augmented()
