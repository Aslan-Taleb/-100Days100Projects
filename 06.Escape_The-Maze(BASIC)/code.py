from library import *

while front_is_clear():
    move()

while not at_goal():
    if right_is_clear():
        turn_right()
        move()
        
        
    elif front_is_clear():
        move()
    else:
        turn_left()
#sound(True)
        
    

        