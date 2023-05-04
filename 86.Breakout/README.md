## BREAKOUT

![Alt text](https://i.imgur.com/7lt3WZa.png)

This code is a python implementation of the popular game Breakout. The game consists of a player controlling a paddle that moves horizontally at the bottom of the screen. The player aims to break all the bricks present on the screen by bouncing a ball off the paddle and the bricks. If the ball falls below the paddle, the player loses one of three lives. The game is won when all the bricks are destroyed.

## Prerequisites

Python 3.x
Turtle Library
Pygame Library

## Getting Started

Clone the repository
Navigate to the directory
Run the main.py file

## How to Play

Use the left and right arrow keys to move the paddle
Use the space key to reset the ball and blocks and start again
Click on the screen to move the paddle to that location

## Code Structure

main.py: Contains the main game loop and integrates all the game components
player.py: Contains the code for the player paddle
ball.py: Contains the code for the game ball
blocks.py: Contains the code for the game blocks
score.py: Contains the code for the score and lives display
library.py: Contains the import statements and the victory(), game_over(), and button_play_again() functions used in the main game loop
