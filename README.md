# Flappy Bird Game

## Project Description
This project is a Python-based clone of the classic Flappy Bird game, developed using the Pygame library. The player controls a bird that must fly between moving green pipes without touching them or the screen boundaries. The bird flaps upward each time the spacebar is pressed and otherwise falls due to gravity. The objective is to survive as long as possible while scoring points for every set of pipes passed.

## Features
- Smooth bird movement with realistic gravity and jump physics
- Randomly generated pipes for endless gameplay
- Real-time scoring system
- “Game Over” and restart functionality
- Simple and visually appealing 2D graphics

## Technologies Used
- Python 3
- Pygame

## How to Play
1. Install Python (3.8 or above).
2. Install the Pygame library (if not installed):
   ```bash
   pip install pygame
   ```
3. Run the game:
   ```bash
   python code.py
   ```
4. Press the SPACEBAR to make the bird flap.
5. Avoid hitting the pipes or the ground to keep playing.
6. When you lose, press SPACEBAR again to restart.

## Game Logic Summary
- The bird constantly falls due to gravity.
- Each spacebar press applies an upward velocity (flap).
- Pipes are generated periodically with random gaps.
- Collisions with pipes or screen edges end the game.
- Score increases each time the bird successfully passes a pipe.

## License
This project is open-source and free to use for educational or personal purposes.
