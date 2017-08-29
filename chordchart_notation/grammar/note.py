# flake8: noqa
from ..parser.parsers.string import String


flat = String('b')
sharp = String('#')

a_step = String('A') | String('a')
b_step = String('B') | String('b')
c_step = String('C') | String('c')
d_step = String('D') | String('d')
e_step = String('E') | String('e')
f_step = String('F') | String('f')
g_step = String('G') | String('g')

note = ( (a_step + ( flat | sharp )['?'])
       | (b_step + ( flat         )['?'])
       | (c_step + (        sharp )['?'])
       | (d_step + ( flat | sharp )['?'])
       | (e_step + ( flat         )['?'])
       | (f_step + (        sharp )['?'])
       | (g_step + ( flat | sharp )['?'])
       ).node('note')
