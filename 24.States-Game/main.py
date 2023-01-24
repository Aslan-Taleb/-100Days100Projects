
from library import *
import time
from art import *
NUMBER_STATE = 50
screen = turtle.Screen()
screen.title("STATES GAME")
image = "USA.gif"
screen.addshape(image)
turtle.shape(image)

game_is_on = True
x = None
y = None

guessed_states = []
answer_to_avoid_bug_cancel = ""
answer_state = ""
say_exit_cheat()
while game_is_on:
    if len(guessed_states) < 50:
        screen.bgcolor("white")
        answer_to_avoid_bug_cancel = screen.textinput(
            title=f"{len(guessed_states)}/{NUMBER_STATE} States Correct", prompt="What's another state's ?")
        if answer_to_avoid_bug_cancel is not None:
            answer_state = answer_to_avoid_bug_cancel.title()
        x, y = check_answer(answer_state)
        if x and y is not None:
            screen.bgcolor("green")
            the_turtle_writer(x, y, answer_state)
            if answer_state not in guessed_states:
                guessed_states.append(answer_state)
        else:
            screen.bgcolor("red")
            time.sleep(0.4)
        x = None
        y = None
    else:
        print("\t\tYou Won ! ")
        print(victory)
        game_is_on = False
    if answer_state == "Exit":
        break
    if answer_state == "Cheat":
        print(cheat)
if game_is_on:
    learn(guessed_states)
