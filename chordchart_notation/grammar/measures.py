from ..parser.parsers.string import String
from ..parser.parsers.separated_by import SeparatedBy

from .chord import chord
from .barline import separator_barline
from .common import whitespace


positive_number = ( String('1')
                  | String('2')
                  | String('3')
                  | String('4')
                  | String('5')
                  | String('6')
                  | String('7')
                  | String('8')
                  | String('9')
                  )

alternative_number = ( positive_number
                     + String('.').skip()
                     ).node('number')

alternative_range = ( positive_number.node('start')
                    + String('-').skip()
                    + positive_number.node('stop')
                    ).node('range')

alternative = ( alternative_number
              | alternative_range
              ).node('alternative')

repeated_measure = ( String('%')
                   | String('%%')
                   ).node('measure_repeat')

chord_continuation = String('/').node('chord_continuation')

measure_element = ( chord
                  | chord_continuation
                  )

normal_measure = SeparatedBy(whitespace['*'], measure_element)

measure = ( alternative['?']
          + whitespace['*']
          + (normal_measure | repeated_measure)
          ).node('measure')

measure_separator = ( whitespace['*']
                    + separator_barline
                    + whitespace['*']
                    )

measures = SeparatedBy(measure_separator, measure)
