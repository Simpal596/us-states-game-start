import turtle
import pandas

screen = turtle.Screen()
# image = "blank_states_img.gif"
# screen.addshape(image)
# turtle.shape(image)

screen.bgpic("blank_states_img.gif")

data = pandas.read_csv("50_states.csv")


score = 0

while score <= 50:
    answer_state = (screen.textinput(title=f"US States Game {score}/50", prompt="Guess Another State:")).title()
    for item in data.state:
        if item == answer_state:
            score += 1
            selected_row = data[data.state == answer_state]
            turtle.hideturtle()
            turtle.penup()
            turtle.goto(int(selected_row.x), int(selected_row.y))
            turtle.write(arg=f"{answer_state}",align="center")
        if answer_state == "Exit":
            break
screen.exitonclick()