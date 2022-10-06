from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color:")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_pos = 0
for color in colors:
    tim = Turtle(shape="turtle")
    tim.penup()
    tim.color(color)
    tim.goto(x=-230, y=-100 + y_pos)
    y_pos += 40

screen.exitonclick()
