from ..parser.parsers.string import String

from .common import whitespace
from .mark import mark


initial_barline_symbol = String('[').node('initial_barline')
final_barline_symbol = String(']').node('final_barline')
initial_repeat_symbol = String('[:').node('initial_repeat_barline')
final_repeat_symbol = String(':]').node('final_repeat_barline')
begin_repeat_symbol = String('|:').node('begin_repeat_barline')
end_repeat_symbol = String(':|').node('end_repeat_barline')
single_barline_symbol = String('|').node('single_barline')
double_barline_symbol = String('||').node('double_barline')

single_barline = ( single_barline_symbol.node('type')
                 + whitespace['*']
                 + mark['?']
                 ).node('barline')

double_barline = ( double_barline_symbol.node('type')
                 + whitespace['*']
                 + mark['?']
                 ).node('barline')

initial_barline = ( initial_barline_symbol.node('type')
                  + whitespace['*']
                  + mark['?']
                  ).node('barline')

final_barline = ( final_barline_symbol.node('type')
                + whitespace['*']
                + mark['?']
                ).node('barline')

initial_begin_repeat = ( initial_repeat_symbol.node('type')
                         + whitespace['*']
                         + mark['?']
                         ).node('barline')

final_repeat = ( final_repeat_symbol.node('type')
                       + whitespace['*']
                       + mark['?']
                       ).node('barline')

begin_repeat_barline = ( begin_repeat_symbol.node('type')
                       + whitespace['*']
                       + mark['?']
                       ).node('barline')

end_repeat_barline = ( end_repeat_symbol.node('type')
                     + whitespace['*']
                     + mark['?']
                     ).node('barline')

part_begin_barline = ( initial_begin_repeat
                     | initial_barline
                     )

part_end_barline = ( final_repeat
                   | final_barline
                   )

separator_barline = ( end_repeat_barline
                    | begin_repeat_barline
                    | double_barline
                    | single_barline
                    )
