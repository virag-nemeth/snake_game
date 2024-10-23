from turtle import Turtle
ALIGNMENT = "center" # Center alignment for text
FONT = ("Courier", 15, "normal") # Font settings for text


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__() # Initialise the Turtle class
        self.score = 0 # Initialise score to zero
        self.color("white") # Set the color of the scoreboard text
        self.penup() # Prevent the scoreboard from drawing lines
        self.goto(0, 270) # Position the scoreboard at the top of the screen
        self.hideturtle()  # Hide the turtle cursor
        self.update_scoreboard() # Display the initial score

    def update_scoreboard(self):
        """Write the current score to the screen"""
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        """Increase the score
        Clear the previous score
        Update the displayed score
        """
        self.score += 1
        self.clear()
        self.update_scoreboard()

    def game_over(self):
        """Display the game over message in the center"""
        self.goto(0,0)
        self.write("GAME OVER", align= ALIGNMENT, font=FONT)
