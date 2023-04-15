import random
from flask import Flask, render_template

app = Flask(__name__)
RANDOM_NUMBER = random.randint(1, 9)


def test_number_decorator(function):
    def wrapped(number):
        global RANDOM_NUMBER
        result = function(number)
        if result > RANDOM_NUMBER:
            return render_template('too_high.html')
        elif result < RANDOM_NUMBER:
            return render_template('too_low.html')
        else:
            RANDOM_NUMBER = random.randint(1, 9)
            return render_template('correct.html')

    return wrapped


@app.route('/')
def start():
    return render_template('index.html')


@app.route("/<int:number>")
@test_number_decorator
def get_number(number):
    return number


if __name__ == "__main__":
    app.run(debug=True)