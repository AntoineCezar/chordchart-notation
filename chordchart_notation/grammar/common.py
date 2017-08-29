from ..parser.parsers.string import String


eol = String('\r\n') | String('\n')
tabulation = String('\t')
space = String(' ')
blank = (space | tabulation)
whitespace = (eol | space | tabulation).skip()
