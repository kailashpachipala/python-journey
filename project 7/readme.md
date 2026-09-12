# 🪨📄✂️ Rock Paper Scissors

A simple command-line **Rock Paper Scissors** game built with Python. The player competes against the computer, which randomly selects Rock, Paper, or Scissors.

## Features

* 🎮 Player vs Computer
* 🎲 Random computer choices
* 🏆 Automatic winner detection
* 📊 Score tracking
* 🤝 Draw detection
* ❌ Input validation
* 🔄 Multiple rounds
* 👋 Quit option
* 🐍 Uses only Python's standard library

## Game Rules

| Player      | Computer    | Result      |
| ----------- | ----------- | ----------- |
| Rock        | Scissors    | Player wins |
| Paper       | Rock        | Player wins |
| Scissors    | Paper       | Player wins |
| Same choice | Same choice | Draw        |

Otherwise, the computer wins.

### Winning Logic

* 🪨 **Rock beats Scissors**
* 📄 **Paper beats Rock**
* ✂️ **Scissors beats Paper**

## Project Structure

```text
rock_paper_scissors/
│
├── rock_paper_scissors.py
├── README.md
└── requirements.txt
```

## Requirements

* Python 3.8 or higher
* No external Python packages are required.

## How to Run

### 1. Clone or download the project

Open a terminal in the project directory.

### 2. Run the program

```bash
python rock_paper_scissors.py
```

On some systems, use:

```bash
python3 rock_paper_scissors.py
```

## How to Play

After starting the program, you will see:

```text
Choose an option:
1. Rock
2. Paper
3. Scissors
4. Quit
```

Enter:

* `1` for Rock
* `2` for Paper
* `3` for Scissors
* `4` to quit

The computer will randomly select its choice and the winner will be displayed.

## Example

```text
========================================
       ROCK PAPER SCISSORS
========================================

Choose an option:
1. Rock
2. Paper
3. Scissors
4. Quit

Enter your choice (1-4): 1

You chose     : Rock
Computer chose: Scissors
🎉 You win!

Score:
You      : 1
Computer : 0
Draws    : 0
```

## Concepts Used

This project is useful for learning basic Python concepts:

* Variables
* Lists
* Dictionaries
* Functions
* `if-elif-else`
* `while` loops
* User input
* String methods
* Random number generation
* Function return values
* Basic program structure

## Python Module Used

The project uses Python's built-in `random` module:

```python
import random
```

No additional installation is necessary.

## Future Improvements

Possible upgrades include:

1. Add **Easy / Medium / Hard** difficulty levels.
2. Add **Best of 3** and **Best of 5** modes.
3. Add player names.
4. Save scores to a file.
5. Create a graphical interface using Tkinter.
6. Add game statistics such as win percentage.
7. Add sound effects.
8. Add Rock/Paper/Scissors emojis to the interface.

## License

This project is free to use for learning and educational purposes.
