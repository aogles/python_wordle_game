
# ANSI COLORS
# https://www.cyberciti.biz/faq/apple-mac-osx-terminal-color-ls-output-option/

# IMPORT REAUIRED FOR RANDOM CHOICE
import os
import random
os.system("clear")
# COLORS
BG_GREEN = "\u001b[42m"
BG_YELLOW = "\u001b[43m"
RESET = "\u001b[0m"

print("LETS PLAY WORDLE")
# word bank for game, all 5 letter words
correct = random.choice(["PAINT", "FEYRE", "ROSES", "COURT", "WINGS"])
# You get six chances to guess
for _ in range(6):
    guess = input("Please guess. > ").upper()

    # Check each letter, will only work with 5 letters
    # will print green background color for letter depending on corect placement
    for i in range(0, 5):
        if guess[i] == correct[i]:
            print(f"{BG_GREEN}{guess[i]}{RESET}", end="")
        elif guess[i] in correct:
            print(f"{BG_YELLOW}{guess[i]}{RESET}", end="")
        else:
            print(guess[i], end="")

    print()

    # Check if the guess is correct
    if guess == correct:
        print("You won wordle!")
        exit()

print("You lose!")
print(f"The correct word was {correct}.")
