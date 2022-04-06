# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line
from ast import Str
from asyncio import BaseTransport

player="Ruud Gullit"
player1="Marco van Basten"
goal_0=32
goal_1=54


scorers = player +" "+str(goal_0)+", "+player1+" "+ str(goal_1)

report=f'{player} scored in the {goal_0}nd minute\n'f'{player1} scored in the {goal_1}th minute'

player="Erwin Koeman" 
first_name=(player[:5]) 
last_name_len=(len(player[6:])) 
name_short=(player[0])+". "+(player[6:])
chant=(first_name+"! ")*4+first_name+"!"
good_chant=(chant[-1] != " ")
