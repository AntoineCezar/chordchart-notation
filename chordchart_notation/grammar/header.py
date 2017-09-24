# flake8: noqa
from ..parser.parsers.string import String
from ..parser.parsers.separated_by import SeparatedBy

from .chord import chord
from .common import eol
from .common import whitespace
from .common import blank
from .common import meter_time


title_key = ( String('title:')
            | String('Title:')
            | String('T:')
            )

title = ( title_key.skip()
        + blank['*'].skip()
        + ~eol['+']
        ).node('title')

composer_key = ( String('composer:')
               | String('Composer:')
               | String('C:')
               )

composer = ( composer_key.skip()
           + blank['*'].skip()
           + ~eol['+']
           ).node('composer')

tone_key = ( String('tone:')
           | String('Tone:')
           )

tone = ( tone_key.skip()
       + blank['*'].skip()
       + chord
       ).node('tone')

meter_key = ( String('meter:')
            | String('Meter:')
            | String('M:')
            )

meter = ( meter_key.skip()
        + meter_time
        ).node('meter')

header = ( SeparatedBy(eol.skip(), ( title
                                   | composer
                                   | tone
                                   | meter
                                   )
                      )
         + eol.skip()
         ).node('header')
