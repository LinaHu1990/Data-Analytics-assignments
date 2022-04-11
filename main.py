# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line
from ast import Str
from asyncio import BaseTransport
from email.utils import localtime

player0="Ruud Gullit"
player1="Marco van Basten"
goal_0=32
goal_1=54
scorers = player0 +" "+str(goal_0)+", "+player1+" "+ str(goal_1)
report=f'{player0} scored in the {goal_0}nd minute\n{player1} scored in the {goal_1}th minute'

#part2
player="Ruud Gullit" 
first_name=player[:player.find(" ")]
last_name_len=len(player[player.find(" ")+1:])
name_short=(player[0])+". "+(player[player.find(" ")+1:])
chant=(first_name+"! ")*(len(first_name)-1) +first_name+"!"
good_chant=(chant[-1] != " ")
