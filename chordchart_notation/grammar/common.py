from ..parser.parsers.string import String


eol = String('\r\n') | String('\n')
tabulation = String('\t')
space = String(' ')
blank = (space | tabulation)
whitespace = (eol | space | tabulation).skip()

meter_number = ( String('2')
               | String('3')
               | String('4')
               | String('5')
               | String('6')
               | String('7')
               | String('8')
               | String('9')
               )

meter_time = ( meter_number
             + String('/')
             + meter_number
             ).node('time')
