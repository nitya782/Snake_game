from turtle import Screen
from scoreboard import ScoreBoard
from snake import Snake
import time
from food import Food

scoreboard = ScoreBoard()
screen = Screen()
screen.setup(width=600, height=600)
screen.title("MY SNAKE GAME")
screen.bgcolor("pink")
screen.tracer(0)

snake = Snake()
food = Food()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.2)
    snake.move()

    if snake.head.distance(food) <= 20:
      food.refresh()
      scoreboard.increase_score()
      snake.extend_snake()

    if snake.head.xcor() > 280  or snake.head.xcor() < -280 or snake.head.ycor()>280 or snake.head.ycor()<-280:
        game_is_on = False
        scoreboard.game_over()

    for seg in snake.segments:
     if seg == snake.head or seg == snake.segments[1] or seg == snake.segments[2] :
        pass
     elif snake.head.distance(seg) < 10:
         game_is_on = False
         scoreboard.game_over()

screen.exitonclick()


