# snake_game
# Snake Game Project

Welcome to my Snake Game! This is a classic version of the Snake game built with Python's Turtle graphics library. The idea is simple: control a snake, eat food, grow longer, and avoid crashing into walls or yourself. This project was all about practicing my OOP (object-oriented programming) skills, so I aimed to keep the code neat and organised.

## How It Works

### Game Basics

- **Goal**: Try to eat as much food as you can without hitting the walls or your own tail!
- **Controls**:
    - Use the **arrow keys** to move the snake up, down, left, or right.
    - Press **"R"** to restart the game when you hit something.

### Game Components

1. **The Snake**:
    - The snake starts with a few segments and gets longer each time it munches on some food.
    - Control the direction using the arrow keys, but watch out! If you bump into yourself or a wall, it's game over.
2. **The Food**:
    - Food appears randomly on the screen. When the snake's head touches the food, it gets a tasty treat, and the food pops up somewhere else.
    - I used a turtle object for the food, which makes it easy to manage and move around.
3. **The Scoreboard**:
    - The scoreboard keeps track of your score and shows it at the top of the screen.
    - If you lose, it’ll display a game over message with your final score and remind you to hit "R" to restart.

### How It's Built

This game uses the **turtle graphics library** in Python, which is perfect for simple games like this. It lets me create and control shapes and images easily, so I can focus on the gameplay.

### OOP in Action

One of the cool things about this project was getting to practice OOP. I set up different classes to handle different parts of the game:

- **Snake Class**: Handles everything about the snake—its movement, growth, and collision detection.
- **Food Class**: Manages where the food appears and how it moves.
- **Scoreboard Class**: Takes care of showing the score and handling game over messages.

Keeping things organised with classes made it way easier to manage everything and plan for future improvements.

## Reflection

Honestly, I faced some pretty frustrating challenges, especially when it came to restarting the game. I had moments where the game over message just wouldn’t go away, and the food wasn’t showing up after a reset.

What I learned from this experience is that sometimes you just need to step back and take a breather. Walking away from my code for a bit helped clear my head. Plus, talking through my struggles with someone else—like my boyfriend—made a huge difference. Even though he doesn’t understand Python, explaining my problem to him helped me see things from a different angle. It’s amazing how much clarity you can gain just by sharing your thoughts.

## Wrap-Up

Building this Snake game was a blast, and I hope you enjoy playing it as much as I enjoyed creating it! Have fun, and happy snaking!
