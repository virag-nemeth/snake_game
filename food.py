from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self): 
        super().__init__()  # Initialize the Turtle class
        self.shape("circle") # Set the shape of the food to a circle
        self.penup() # Prevent the food from drawing lines when it moves
        self.shapesize(stretch_len=0.5,stretch_wid=0.5) # Resize the food
        self.color("orange") # Set the color of the food
        self.speed("fastest") # Set the drawing speed to the fastest
        self.refresh() # Place the food at a random position

    def refresh(self):
        """ Generate random coordinates for the food within the screen bounds"""
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x,random_y) # Move the food to the new coordinates
        print(f"Food position: ({random_x}, {random_y})")  # Debugging line
