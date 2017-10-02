===================
Chordchart Notation
===================

Text based chordchart notation.

===========
Quick Start
===========

.. code::

    cd <dicrectory containing this file>
    python setup.py install
    chordchart-to-html mychordchat.txt
    $BROWSER mychordchat.html

To learn how to write your own chordcharts, you can either:

    * look at provided exemples in the examples directory
    * try to understand the associated grammar (good luck)

================
Language Grammar
================

.. code::

    chordchart              = header? body?
    header                  = header_field (eol header_field)*
    header_field            = title | composer | tone | meter
    title                   = title_key blank* title_value
    title_key               = "title:" | "Title:" | "T:"
    title_value             = ~eol+
    composer                = composer_key blank* composer_value
    composer_key            = "composer:" | "Composer:" | "C:"
    composer_value          = ~eol+
    tone                    = tone_key blank* chord
    tone_key                = "tone:" | "Tone:"
    meter                   = meter_key blank* meter_time
    meter_key               = "meter:" | "Meter:" | "M:"
    meter_time              = [2-9] "/" [2-9]
    blank                   = space | tabulation
    space                   = " "
    tabulation              = "\t"
    eol                     = "\r\n" | "\n"
    chord                   = chord_root chord_kind? chord_bass? mark?
    chord_root              = note
    chord_kind              = minor_sixth
                            | minor_seventh
                            | minor_nineth
                            | minor_eleventh
                            | minor_thirteenth
                            | minor
                            | suspended_second
                            | suspended_fourth
                            | sixth
                            | major_seventh
                            | seventh
                            | nineth
                            | eleventh
                            | thirteenth
                            | half_diminished
                            | diminished
                            | augmented
    chord_bass              = "/" note
    minor_sixth             = minor sixth
    minor_seventh           = minor seventh
    minor_nineth            = minor nineth
    minor_eleventh          = minor eleventh
    minor_thirteenth        = minor thirteenth
    minor                   = "min" | "m" | "-"
    suspended_second        = suspended second
    suspended_fourth        = suspended fourth
    suspended               = "sus"
    second                  = "2"
    fourth                  = "4"
    sixth                   = "6"
    major_seventh           = "7M" | "M7"
    seventh                 = "7"
    nineth                  = "9"
    eleventh                = "11"
    thirteenth              = "13"
    half_diminished         = "hdim" | "ø" | "Ø"
    diminished              = "dim" | "°"
    augmented               = "aug" | "+"
    mark                    = segno_symbol | coda_symbol
    segno_symbol            = "!S" | "!segno!"
    coda_symbol             = "!C" | "!coda!"
    body                    = parts?
    parts                   = part (whitespace* part)*
    part                    = part_begin measures whitespace* part_end_barline
    part_begin              = part_label? part_begin_barline whitespace*
    part_label              = part_label_key part_label_value
    part_label_key          = 'P:' blank*
    part_label_value        = [A-Z] eol+
    whitespace              = eol | space | tabulation
    measures                = measure (measure_separator measure)*
    measure                 = alternative? whitespace* (normal_measure | repeated_measure)
    alternative             = alternative_number | alternative_range
    alternative_number      = [1-9]
    alternative_range       = [1-9] "-" [1-9]
    normal_measure          = measure_element (whitespace* measure_element)*
    measure_element         = chord | chord_continuation
    chord_continuation      = "/"
    repeated_measure        = "%" | "%%"
    measure_separator       = whitespace* separator_barline whitespace*
    separator_barline       = end_repeat_barline
                            | begin_repeat_barline
                            | double_barline
                            | single_barline
    part_begin_barline      = initial_begin_repeat | initial_barline
    part_end_barline        = final_repeat | final_barline
    single_barline          = single_barline_symbol whitespace* mark?
    double_barline          = double_barline_symbol whitespace* mark?
    initial_barline         = initial_barline_symbol whitespace* mark?
    final_barline           = final_barline_symbol whitespace* mark?
    initial_begin_repeat    = initial_repeat_symbol whitespace* mark?
    final_repeat            = final_repeat_symbol whitespace* mark?
    begin_repeat_barline    = begin_repeat_symbol whitespace* mark?
    end_repeat_barline      = end_repeat_symbol whitespace* mark?
    initial_barline_symbol  = "["
    final_barline_symbol    = "]"
    initial_repeat_symbol   = "[:"
    final_repeat_symbol     = ":]"
    begin_repeat_symbol     = "|:"
    end_repeat_symbol       = ":|"
    single_barline_symbol   = "|"
    double_barline_symbol   = "||"
