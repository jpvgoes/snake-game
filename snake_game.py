from turtle import Screen
from time import sleep
from snake import Snake
from food import Food
from scoreboard import ScoreBoard

screen = Screen()
screen.setup(600,600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = ScoreBoard()

screen.update()


screen.listen()
screen.onkeypress(snake.up,"Up")
screen.onkeypress(snake.down,"Down")
screen.onkeypress(snake.left,"Left")
screen.onkeypress(snake.right,"Right")


game_is_on = True

while game_is_on:
    screen.update()
    sleep(0.1)

    #aqui faz os pedaços da cobra seguirem uns aos outros
    snake.move()

    #detectar colisão com a comida
    if snake.head.distance(food) < 15:
        print("comeu")
        snake.extend()
        scoreboard.increase_score()
        food.refresh()

    #detectar colisão com a parede
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        scoreboard.game_over()

    #detectar colisão com o rabo
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()







screen.exitonclick()