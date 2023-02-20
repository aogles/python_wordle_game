
from random import choice

words_bank = ['FEYRE', 'DARLING', 'RHYSAND',
              'AZRIEL', 'CASSIAN', 'TAMPON', 'LUCIEN', 'COURT']

SQUARES = {
    'correct_place': '🟩',
    'correct_letter': '🟨',
    'incorrect_letter': '⬛'
}

WELCOME_MESSAGE = f'\n WELCOME TO WORDLE \n'

player_instructions = "Start guessing \n"
input_guess = "Enter your guess"
tries = 6

chosen_word = choice(words_bank)
print(WELCOME_MESSAGE)
print(player_instructions)
print(tries)


def correct_place(letter):
    return f'[black on green]{letter}[/]'


def correct_letter(letter):
    return f'[black on yellow]{letter}[/]'


def incorrect_letter(letter):
    return f'[black on white]{letter}[/]'


def check_guess(guess, answer):
    guessed = []
    wordle_pattern = []
    for i, letter in enumerate(guess):
        if answer[i] == guess[i]:
            guessed += correct_place(letter)
            wordle_pattern.append(SQUARES['correct_place'])
        elif letter in answer:
            guessed += correct_letter(letter)
            wordle_pattern.append(SQUARES['correct_letter'])
        else:
            guessed += incorrect_letter(letter)
            wordle_pattern.append(SQUARES['incorrect_letter'])
    return ''.join(guessed), ''.join(wordle_pattern)


def game(chosen_word):
    end_of_game = False
    already_guessed = []
    full_wordle_pattern = []
    all_words_guessed = []

    while not end_of_game:
        guess = (input_guess).upper()
        while len(guess) != 5 or guess in already_guessed:
            if guess in already_guessed:
                print("[red]You've already guessed this word!!\n[/]")
            else:
                print('[red]Please enter a 5-letter word!!\n[/]')
            guess = (input_guess).upper()
        already_guessed.append(guess)
        guessed, pattern = check_guess(guess, chosen_word)
        all_words_guessed.append(guessed)
        full_wordle_pattern.append(pattern)

        print(*all_words_guessed, sep="\n")
        if guess == chosen_word or len(already_guessed) == tries:
            end_of_game = True
    if len(already_guessed) == tries and guess != chosen_word:
        print(f"\n[red]WORDLE X/{tries}[/]")
        print(f'\n[green]Correct Word: {chosen_word}[/]')
    else:
        print(
            f"\n[green]WORDLE {len(already_guessed)}/{tries}[/]\n")
        print(*full_wordle_pattern, sep="\n")


if __name__ == '__main__':
    chosen_word = choice(words_bank)
