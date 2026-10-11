HANGMAN GAME
A simple text-based word guessing game in Python

Description
----------
Hangman is a console game where the computer secretly picks a
word and the player guesses it one letter at a time. The word
is shown as blanks (_ _ _ _ _), and correct guesses reveal the
letter in every position where it appears. The player is allowed
a maximum of 6 incorrect guesses.

Features
--------
Random word chosen from 5 predefined words
Hint at the start of the game showing the first letter of the word
Word progress displayed after every guess
Maximum of 6 incorrect guesses
Input validation (single letters only, case-insensitive)
Repeated guesses are detected and do not cost a life
Win and lose messages that reveal the secret word

Key Concepts Used
-----------------
random module  : choosing the secret word
while loop   : running turns until the game ends
if-else     : checking guesses and game status
strings     : handling the word and letters
lists      : storing the word list and guessed letters

Requirements
------------
Python 3.8 or newer
No external libraries needed (only the built-in random module)

How To Run
----------
Download or clone this project.
Open a terminal in the project folder.
Run:

python hangman.py

(On some systems use: python3 hangman.py)

How To Play
-----------
A hint shows the first letter of the word, and the word is
shown as underscores, one per letter.
Type one letter and press Enter.
If the letter is in the word, it is revealed.
If not, you lose one life (you have 6).
Win by revealing the full word before running out of lives.
Invalid input (numbers, symbols, several letters) and
repeated letters do not cost a life.

Sample Output
-------------
============== WELCOME TO HANGMAN Game ==============
Hint:
The word starts with: p

Word: _ _ _ _ _ _
Guessed:
Guess a letter: p
Correct!

Word: p _ _ _ _ _
Guessed: p
Guess a letter: z
Wrong! Lives left: 5

... (game continues) ...

You won! The word was 'python'.

Project Structure
-----------------
hangman-game/
|-- hangman.py  (main game code)
|-- README.txt  (this file)

Possible Improvements
---------------------
Optional extra hints (e.g. word length or category)
ASCII hangman drawing that updates with each wrong guess
"Play again?" option after each game
Difficulty levels or word categories
Load words from a file

Author
------
Name: Gireeshwarareddy
Created as part of a Python programming internship task.