import turtle
import pandas

data = pandas.read_csv('50_states.csv')


def check_answer(answer_state):
    if not data[data['state'] == answer_state].empty:
        x = int(data[data['state'] == answer_state]['x'])
        y = int(data[data['state'] == answer_state]['y'])
        return x, y
    else:
        return None, None


def the_turtle_writer(x, y, answer_state):
    timmy = turtle.Turtle()
    timmy.hideturtle()
    timmy.penup()
    timmy.goto(x, y)
    timmy.write(answer_state, align='center', font=("Arial", 10, "normal"))


def learn(guessed_states):
    state_to_learn = []
    message = "Hey,you haven't found a 'few' states, I'll put you the list to learn what you have left : \n"
    all_states = data['state'].to_list()
    state_to_learn = [
        state for state in all_states if state not in guessed_states]
    for i in state_to_learn:
        message += i + "\n"
    message += "Good Luck ! "
    print(message)


def say_exit_cheat():
    timmy = turtle.Turtle()
    timmy.hideturtle()
    timmy.penup()
    timmy.goto(250, -300)
    timmy.write("Type 'exit' to Exit.\nType 'cheat' to cheat.", align='center',
                font=("Arial", 10, "normal"))
