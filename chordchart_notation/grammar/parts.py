# flake8: noqa
from ..parser.parsers.string import String
from ..parser.parsers.any_of import AnyOf
from ..parser.parsers.separated_by import SeparatedBy

from .barline import part_begin_barline
from .barline import part_end_barline
from .common import whitespace
from .common import eol
from .common import blank
from .measures import measures

capital_letter = AnyOf('A', 'B', 'C', 'D',
                       'E', 'F', 'G', 'H',
                       'I', 'J', 'K', 'L',
                       'M', 'N', 'O', 'P',
                       'Q', 'R', 'S', 'T',
                       'U', 'V', 'W', 'X',
                       'Y', 'Z')

part_label = ( String('P:').skip()
             + blank['*'].skip()
             + capital_letter
             + eol['+'].skip()
             ).node('label')

part = ( part_label['?']
       + part_begin_barline
       + whitespace['*']
       + measures
       + whitespace['*']
       + part_end_barline
       ).node('part')

parts = SeparatedBy(whitespace['*'], part)
