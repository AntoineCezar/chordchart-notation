# flake8: noqa
from ..parser.parsers.string import String
from ..parser.parsers.separated_by import SeparatedBy

from .header import header
from .parts import parts


body = ( parts['?']
       ).node('body')

chordchart = ( header['?']
             + body['?']
             ).node('chordchart')
