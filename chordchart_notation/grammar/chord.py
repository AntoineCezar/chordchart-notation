# flake8: noqa
from ..parser.parsers.string import String

from .note import note
from .mark import mark


minor = ( String('min')
        | String('m')
        | String('-')
        )

second = String('2')

fourth = String('4')

sixth = String('6')

seventh = String('7')

major_seventh = ( String('M7')
                | String('7M')
                )

nineth = String('9')

eleventh = String('11')

thirteenth = String('13')

suspended = String('sus')

augmented = ( String('aug')
            | String('+')
            )

half_diminished = ( String('hdim')
                  | String('ø')
                  | String('Ø')
                  )

diminished = ( String('dim')
             | String('°')
             )

chord_root = note.node('root')

chord_kind = ( ( minor + sixth ).node('minor_sixth')
             | ( minor + seventh ).node('minor_seventh')
             | ( minor + nineth ).node('minor_nineth')
             | ( minor + eleventh ).node('minor_eleventh')
             | ( minor + thirteenth ).node('minor_thirteenth')
             | minor.node('minor')
             | ( suspended + second ).node('suspended_second')
             | ( suspended + fourth ).node('suspended_fourth')
             | sixth.node('sixth')
             | major_seventh.node('major_seventh')
             | seventh.node('seventh')
             | nineth.node('nineth')
             | eleventh.node('eleventh')
             | thirteenth.node('thirteenth')
             | half_diminished.node('half_diminished')
             | diminished.node('diminished')
             | augmented.node('augmented')
             ).node('kind')

chord_bass = ( String('/').skip()
             + note
             ).node('bass')

chord = ( chord_root
        + chord_kind['?']
        + chord_bass['?']
        + mark['?']
        ).node('chord')
