from turtle import Turtle
STARTING_POSITIONS = [(0,0), (-20,0), (-40,0)] # Starting positions of the snake segments
MOVE_DISTANCE = 20 # Distance the snake moves
UP = 90 # Heading for moving up
DOWN = 270 # Heading for moving down
LEFT = 180 # Heading for moving left
RIGHT = 0 # Heading for moving right


class Snake:

    def __init__(self):
        self.segments = [] # List to hold the snake segments
        self.create_snake() # Create the initial snake
        self.head = self.segments[0] # Set the head of the snake

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position) # Add each segment to the snake

    def move(self):
        """Move the segments of the snake"""
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def add_segment(self,position):
        new = Turtle(shape="square") # Create a new segment
        new.color("white") # Set the color of the segment
        new.penup() # Prevent the segment from drawing lines
        new.goto(position) # Position the segment
        self.segments.append(new) # Add the segment to the list


    def extend(self):
        #add a new segment to the snake
        self.add_segment(self.segments[-1].position()) # Use the position of the last segment


    def up(self):
        """# Change the direction of the snake to up"""
        if self.head.heading() != DOWN: # Prevent the snake from moving in the opposite direction
            self.head.setheading(UP)

    def down(self):
        """Change the direction of the snake to down"""
        if self.head.heading() != UP: # Prevent the snake from moving in the opposite direction
            self.head.setheading(DOWN)

    def left(self):
        """Change the direction of the snake to left"""
        if self.head.heading() != RIGHT: # Prevent the snake from moving in the opposite direction
            self.head.setheading(LEFT)

    def right(self):
        """Change the direction of the snake to right"""
        if self.head.heading() != LEFT: # Prevent the snake from moving in the opposite direction
            self.head.setheading(RIGHT)

    def restart(self):
        # Clear existing segments and recreate the snake
        for segment in self.segments:
            segment.hideturtle()  # Hide each segment
        self.segments.clear()  # Clear the list of segments
        self.create_snake()  # Create a new snake
        self.head = self.segments[0]  # Set the head to the new first segmentt





