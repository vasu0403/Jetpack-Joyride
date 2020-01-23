# Jetpack Joyride in Python 3
This is a terminal version of Jetpack Joyride written in python3 using basic libraries. The game is written using OOPS concepsts of Inheritence, Polymorphism, Encapsulation and Abstraction.

### Structure of game
- The entire game is in the form of 2-Dimensional vector which is built using numpy library of python.
- Each cell of the vector is a class object and contains some basic properties which are shared by all the objects in the game
- Different objects inherent from the base parent class and manipulate the desired properties.

### Features
- Gravity fall
- Fire beams
- Coins
- Magnets
- Speed Boosts
- Shield
- Boss Dragon

### Running the program
1. Install all the requirements
```sh
    pip install -r requirements.txt
```
2. Run the program
```sh
    python3 game.py
```
### Controls
- Press W to fly
- Press A to move left
- Press D to move right
- Press S to move downwards
- Press E to show bullets
- Press SPACE to activate shield (when available)

