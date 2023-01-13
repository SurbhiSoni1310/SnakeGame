from turtle import Turtle, Screen
from time import sleep
from snake import Snake
from food import Food
from score_board import Score

s = Screen()
s.setup(width=600, height=600)
s.bgcolor("black")
s.title("My Snake Game")
s.tracer(0)
snake = Snake()
food = Food()
Score_Board = Score()
s.listen()
s.onkey(snake.up, "Up")
s.onkey(snake.down, "Down")
s.onkey(snake.right, "Right")
s.onkey(snake.left, "Left")
game_is_on = True
while game_is_on:
    s.update()
    snake.move()
    # detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        Score_Board.update()
        snake.extend()

    # detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        Score_Board.reset_score()
        snake.reset_snake()

    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            Score_Board.reset_score()
            snake.reset_snake()

    sleep(0.1)
s.exitonclick()
