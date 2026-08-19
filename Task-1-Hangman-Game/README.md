# 🎮 Hangman Game

## 📌 Project Overview

**Hangman Game** is a simple text-based word guessing game developed using Python. The player has to guess a randomly selected word one letter at a time.

The player gets a limited number of incorrect attempts. The game ends when the player successfully guesses the complete word or uses all available incorrect attempts.

This project demonstrates the use of Python fundamentals including **loops, conditional statements, strings, lists, functions, random selection, and input validation**.

---

## 🎯 Project Objective

The objective of this project is to develop an interactive command-line game while applying core Python programming concepts.

The game provides a simple and engaging way to practice:

* Random selection
* String manipulation
* Lists
* Loops
* Conditional statements
* Functions
* User input validation

---

## 🚀 Features

* 🎲 Random word selection
* 📚 5 predefined words
* ❤️ Maximum 6 incorrect guesses
* 🔤 Letter-by-letter guessing
* 🛡️ Input validation
* 🚫 Prevents repeated guesses
* 🏆 Win condition
* 💀 Lose condition
* 🖥️ Interactive command-line interface

---

## 🛠️ Technologies Used

| Technology             | Purpose                                    |
| ---------------------- | ------------------------------------------ |
| Python 3               | Core programming language                  |
| `random` module        | Random word selection                      |
| Lists                  | Store predefined words and guessed letters |
| Strings                | Word and character processing              |
| Loops                  | Game execution                             |
| Conditional Statements | Game logic and win/lose conditions         |
| Functions              | Organizing program logic                   |

---

## 📂 Project Structure

```text
Hangman-Game/
│
├── hangman.py
└── README.md
```

### File Description

**`hangman.py`**

Contains the complete Hangman game logic.

**`README.md`**

Contains project documentation, features, setup instructions, and usage information.

---

## ⚙️ Game Workflow

```text
                Start
                  │
                  ▼
          Select Random Word
                  │
                  ▼
          Display Hidden Word
                  │
                  ▼
          Ask User for Letter
                  │
                  ▼
          Validate User Input
                  │
                  ▼
        Is Letter in the Word?
             /           \
           Yes            No
            │              │
            ▼              ▼
      Reveal Letter    Reduce Attempts
            │              │
            └──────┬───────┘
                   ▼
          Check Game Status
             /          \
          Win             Lose
           │               │
           ▼               ▼
       Game Over       Game Over
```

---

## 🎮 How to Play

1. Run the Python program.
2. The program randomly selects a word.
3. The selected word is hidden from the player.
4. Enter one letter at a time.
5. If the letter exists in the word, it is revealed.
6. If the letter is incorrect, one attempt is lost.
7. You can make a maximum of **6 incorrect guesses**.
8. Guess the complete word before running out of attempts to win.

---

## ▶️ How to Run

### Step 1 — Install Python

Make sure Python 3 is installed on your system.

Check the installation:

```bash
python --version
```

### Step 2 — Open the Project Folder

Open Terminal or PowerShell inside the project folder.

```bash
cd Hangman-Game
```

### Step 3 — Run the Game

```bash
python hangman.py
```

---

## 🧪 Example Gameplay

```text
================================
        HANGMAN GAME
================================

Guess the word:

_ _ _ _ _

Incorrect guesses remaining: 6

Enter a letter: p

Correct!

_ p _ _ _

Enter a letter: x

Incorrect guess!

Incorrect guesses remaining: 5
```

The game continues until the player guesses the word or runs out of attempts.

---

## 🛡️ Input Validation

The program validates user input to ensure:

* Only a single character is entered.
* Alphabetic characters are accepted.
* Previously guessed letters are not accepted again.
* Invalid inputs display an appropriate message.

---

## 🏆 Game Conditions

### Winning Condition

The player wins when all letters of the hidden word have been correctly guessed.

Example:

```text
Word: PYTHON

P Y T H O N

Congratulations! You Won!
```

### Losing Condition

The player loses when all 6 incorrect attempts are used.

```text
Incorrect guesses remaining: 0

Game Over!
The correct word was: PYTHON
```

---

## 📚 Python Concepts Demonstrated

This project demonstrates:

* Variables
* Strings
* Lists
* Sets
* Functions
* `if-else` statements
* `while` loops
* `for` loops
* User input
* Random selection
* String manipulation
* Input validation

---

## 🔮 Future Improvements

The game can be enhanced with:

* 🎯 Difficulty levels
* 📚 Larger word database
* 🏆 Score system
* ❤️ Visual Hangman stages
* 🔄 Play Again option
* 📂 Word selection from external files
* 👥 Two-player mode
* ⏱️ Time-based challenges
* 🎨 Colored terminal interface

---

## 📈 Learning Outcomes

Through this project, the following skills were practiced:

* Building an interactive CLI application
* Using Python's `random` module
* Managing strings and lists
* Implementing loops and conditions
* Validating user input
* Designing game logic
* Handling different game states

---

# 📌 GitHub Setup

If you want to upload this project to GitHub, use the following commands:

```bash
git init

git add .

git commit -m "Initial Commit - Hangman Game"

git branch -M main

git remote add origin YOUR_REPO_LINK

git push -u origin main
```

Replace:

```text
YOUR_REPO_LINK
```

with your actual GitHub repository URL.

---

## 👨‍💻 Author

**Aditya Keshri**

B.Tech CSE Student

---

## 📌 Project Information

**Project:** Hangman Game

**Task:** Python Internship Task

**Language:** Python 3

**Project Type:** Command-Line Game
