from turtle import Screen
from scoreboard import Scoreboard
from snake import Snake
from food import Food
import time

# Set up the game screen
screen = Screen()
screen.setup(600,600) # Set the size of the screen
screen.bgcolor("black") # Set the background color to black
screen.title("Snake Game") # Set the title of the window
screen.tracer(0) # Disable automatic screen updates for manual control

# Create instances of the game components
snake = Snake()
food = Food()
scoreboard = Scoreboard()

# Set up controls for the snake
screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

# Control the game loop
game_is_on = True
while game_is_on:
    screen.update() # Update the screen
    time.sleep(0.1) # Control the speed of the game
    snake.move() # Move the snake

    #Detect collision with food
    if snake.head.distance(food) < 15: # If the snake's head is close to the food
        food.refresh() # Move the food to a new position
        snake.extend() # Add a segment to the snake
        scoreboard.increase_score() # Update the score

    #Detect collision with wall
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        game_is_on = False # End the game if the snake hits the wall
        scoreboard.game_over() # Display game over message

    #Detect collision with tail
    for segment in snake.segments[1:]: # Check each segment of the snake except the head
        if snake.head.distance(segment) < 10: # If the head collides with a segment
            game_is_on = False # End the game
            scoreboard.game_over() # Display game over message













screen.exitonclick()