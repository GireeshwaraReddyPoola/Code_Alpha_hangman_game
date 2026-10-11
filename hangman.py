import random


words = ["Mouse", "Moniter", "CPU", "keyboard", "Speaker"]
secret_word = random.choice(words).lower()


guessed_letter=[]
max_chance=6
wrong_guess=0
print("============== WELCOME TO HANGMAN Game ==============")
print("Hint:\nThe word starts with:", secret_word[0])

while wrong_guess < max_chance:
    display=""
    for letter in secret_word:
        if letter in guessed_letter:
            display+=letter+" "
        else:
            display+="_"+" "
    print("\nWord:", display)
    print("Guessed:", " ".join(guessed_letter))
    guess = input("Guess a letter: ").lower()
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single letter.")
        continue
    if guess in guessed_letter:
        print("You already guessed that letter.")
        continue

    guessed_letter.append(guess)
    if guess in secret_word:
        print("Correct!")
    else:
        wrong_guess += 1
        print(f"Wrong! Lives left: {max_chance - wrong_guess}")
    all_guessed = True
    for letter in secret_word:
        if letter not in guessed_letter:
            all_guessed = False
            break
    if all_guessed:
        print(f"\nCongratulations! \nYou won! \nThe word was '{secret_word}'.")
        break
else:
    print(f"\nGame over!\nBetter Luck Next Time! \nThe word was '{secret_word}'.")


