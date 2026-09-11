# 🎯 Number Guessing Game

A simple and interactive **Number Guessing Game built with Python**.
The computer randomly selects a number, and the player must guess it within a limited number of attempts.

The game includes **Easy, Medium, and Hard difficulty levels**, hints, scoring, and a play-again option.

## ✨ Features

* 🎚️ Three difficulty levels:

  * **Easy:** 1–50, 10 attempts
  * **Medium:** 1–100, 7 attempts
  * **Hard:** 1–200, 5 attempts
* 🎲 Random number generation
* 💡 Automatic hints
* 🏆 Score system
* 🔄 Play again option
* 📊 Attempt tracking
* ❌ Game-over message when attempts are exhausted
* 👋 Displays final score when the player exits

## 🛠️ Technologies Used

* **Python 3**
* `random` module
* Conditional statements (`if`, `elif`, `else`)
* `for` loop
* `while` loop
* User input
* Basic arithmetic

## 📁 Project Structure

```text
Number-Guessing-Game/
│
├── number_guessing_game.py
└── README.md
```

## ⚙️ How to Run

### 1. Install Python

Make sure Python 3 is installed on your computer.

Check the Python version:

```bash
python --version
```

### 2. Download or Clone the Project

Clone the repository:

```bash
git clone https://github.com/your-username/number-guessing-game.git
```

Move into the project folder:

```bash
cd number-guessing-game
```

### 3. Run the Game

```bash
python number_guessing_game.py
```

## 🎮 How to Play

### Step 1: Select Difficulty

The game displays three options:

```text
1. Easy   → 1 to 50, 10 attempts
2. Medium → 1 to 100, 7 attempts
3. Hard   → 1 to 200, 5 attempts
```

Choose your preferred difficulty.

### Step 2: Guess the Number

Enter a number within the selected range.

The game will tell you whether your guess is:

* 📉 **Too low**
* 📈 **Too high**
* 🎉 **Correct**

### Step 3: Use Hints

If you haven't guessed the number after several attempts, the game provides hints.

For example:

```text
💡 Hint: The number is EVEN.
```

or:

```text
💡 Hint: The number is greater than 50.
```

### Step 4: Earn Points

The fewer attempts you use, the more points you receive.

```text
Points = (Maximum Attempts - Attempts Used + 1) × 10
```

## 🧪 Example Output

```text
🎯 WELCOME TO NUMBER GUESSING GAME 🎯

Choose Difficulty:
1. Easy   → 1 to 50, 10 attempts
2. Medium → 1 to 100, 7 attempts
3. Hard   → 1 to 200, 5 attempts

Enter your choice (1/2/3): 2

🎮 Difficulty: Medium
Guess a number between 1 and 100
You have 7 attempts.

Attempt 1: Enter your guess: 50
📉 Too low! Try a higher number.

Attempt 2: Enter your guess: 75
📈 Too high! Try a lower number.

Attempt 3: Enter your guess: 63
🎉 CONGRATULATIONS!

Correct number: 63
Attempts used: 3
⭐ Points earned: 50
🏆 Total Score: 50
```

## 🧠 Concepts Learned

This project helps beginners understand:

* Variables
* Data types
* `input()` and output
* `if-elif-else`
* `for` loops
* `while` loops
* `break`
* Random number generation
* Arithmetic operations
* String methods
* Basic game logic

## 🚀 Future Improvements

The game can be improved by adding:

* 🔐 Input validation for invalid numbers
* 👤 Player names
* 🥇 High-score leaderboard
* ⏱️ Timer-based gameplay
* 🎨 Graphical User Interface (GUI) using Tkinter
* 🔊 Sound effects
* 📈 Game statistics
* 👥 Two-player mode

## 📌 Project Type

**Beginner Python Mini Project**

## 👨‍💻 Author

**Your Name**

Feel free to modify and improve this project!

## 📄 License

This project is created for **educational and learning purposes**.
