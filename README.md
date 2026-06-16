Hangman Game

Project Overview

The Hangman Game is a console-based Python project developed as part of the CodeAlpha Internship. It is a classic word-guessing game that helps beginners understand the fundamentals of Python programming through an interactive application.

In this game, the computer randomly selects a word from a predefined list, and the player must guess the word one letter at a time. For every incorrect guess, the player loses one attempt. The player has a maximum of 6 incorrect guesses to identify the hidden word. If the player successfully guesses all the letters before reaching the maximum limit, they win; otherwise, the game ends and the correct word is displayed.

Objectives

- To develop a simple command-line game using Python.
- To improve logical thinking and problem-solving skills.
- To understand how loops, conditional statements, lists, and string operations work together in a real-world application.
- To gain practical experience with Python programming.

Features

- Randomly selects a word from a predefined list using the "random" module.
- Displays hidden letters using underscores ("_").
- Accepts one letter as input from the user.
- Reveals correctly guessed letters in their respective positions.
- Tracks previously guessed letters to prevent duplicate inputs.
- Allows a maximum of 6 incorrect guesses.
- Displays appropriate messages for correct and incorrect guesses.
- Shows a Congratulations message when the player wins.
- Displays Game Over and reveals the correct word if all attempts are used.

Python Concepts Used

- Variables
- Lists
- Strings
- For Loop
- While Loop
- Conditional Statements ("if", "elif", "else")
- User Input ("input()")
- Random Module ("random.choice()")
- List Methods ("append()")
- String Methods ("join()", "lower()")
- Functions ("len()", "range()")

Project Workflow

1. Import the "random" module.
2. Create a list of words.
3. Randomly select one word from the list.
4. Display underscores representing each letter of the word.
5. Initialize the wrong guess counter and guessed letters list.
6. Accept one letter as input from the user.
7. Check whether the letter has already been guessed.
8. If the letter exists in the word, reveal its position(s).
9. If the letter is incorrect, increase the wrong guess count.
10. Continue the game until the player guesses the word or reaches six incorrect guesses.
11. Display the final result (Win or Game Over).

Technologies Used

- Python 3
- Command Line Interface (CLI)

How to Run

1. Download or clone this repository.
2. Open the project folder in a terminal or command prompt.
3. Run the following command:

python hangman.py

Output

- Displays the hidden word using underscores.
- Accepts user guesses one letter at a time.
- Updates the word after each correct guess.
- Shows the remaining incorrect attempts.
- Displays either Congratulations! You guessed the word. or Game Over! The correct word was: ...

Author

Hema

Developed as part of the CodeAlpha Python Programming Internship.
