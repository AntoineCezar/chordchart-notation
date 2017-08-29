from ..parser.parsers.string import String


segno_symbol = ( String('!S')
               | String('!segno!')
               ).node('segno_symbol')

coda_symbol = ( String('!C')
              | String('!coda!')
              ).node('coda_symbol')

mark = ( segno_symbol
       | coda_symbol
       ).node('mark')
