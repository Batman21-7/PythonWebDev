from flask import Flask
from random import randint

random_num = randint(0, 9)

app = Flask(__name__)


@app.route("/")
def index():
    return ('<h1>Guess a number between 0 and 9</h1>'
            '<img src= "https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExNmUwdWIyMGhqamdzeWdhaGlyMWxpcnk5eTdqODBwc2g3Y3lycWE4MyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/qrIlvM63x7x9IjrHw1/giphy.gif">')


@app.route("/<int:user_number>")
def redirect(user_number):
    if user_number < random_num:
        return ('<h1 style="color: red">Too low, try again!</h1>'
                '<img src="https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif">')
    elif user_number > random_num:
        return ('<h1 style="color: purple">Too high, try again!</h1>'
                '<img src="https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif">')
    else:
        return ('<h1 style="color: green">You found me!</h1>'
                '<img src="https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif">')


if __name__ == "__main__":
    app.run(debug=True)
