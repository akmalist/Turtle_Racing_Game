from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(500, 400)
user_bet = screen.textinput(title = 'Make your bet', prompt='Which turtle will win the race? Enter Color: ')

colors = ['red', 'yellow', 'blue', 'green', 'purple', 'pink']

all_turtles = []

start = -70

for each_turtle in range(0, 6):
    new_turtle = Turtle('turtle')
    new_turtle.penup()
    new_turtle.goto(-230, start)
    start += 30
    new_turtle.color(colors[each_turtle])
    all_turtles.append(new_turtle)


if user_bet:
    gameOn = True

while gameOn:
    for each_turtle in all_turtles:
        if each_turtle.xcor() > 230:
            gameOn = False
            winning_color = each_turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner")
        random_move = random.randint(0, 10)
        each_turtle.forward(random_move)


# def move_forward():
#     tim.forward(15)
#
#
# def move_backwards():
#     tim.backward(20)
#
# def move_counter():
#     tim.left(20)
#
# def move_clock():
#     tim.right(20)
#
# def clean():
#     tim.clear()
#     tim.reset()
#     tim.home()
#
# screen.listen()
# screen.onkey(key="w", fun=move_forward)
# screen.onkey(key='s', fun=move_backwards)
# screen.onkey(key="a", fun=move_counter)
# screen.onkey(key='d', fun=move_clock)
# screen.onkey(key='c', fun=clean)
screen.exitonclick()
