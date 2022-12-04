"""Hangman, by Al Sweigart al@inventwithpython.com
Guess the letters to a secret word before the hangman is drawn.
This code is available at https://nostarch.com/big-book-small-python-programming
Tags: large, game, word, puzzle"""

# A version of this game is featured in the book "Invent Your Own
# Computer Games with Python" https://nostarch.com/inventwithpython

import random, sys

# Set up the constants:
# (!) Try adding or changing the strings in HANGMAN_PICS to make a
# guillotine instead of a gallows.
HANGMAN_PICS = [r"""
 +--+
 |  |
    |
    |
    |
    |
=====""",
r"""
 +--+
 |  |
 O  |
    |
    |
    |
=====""",
r"""
 +--+
 |  |
 O  |
 |  |
    |
    |
=====""",
r"""
 +--+
 |  |
 O  |
/|  |
    |
    |
=====""",
r"""
 +--+
 |  |
 O  |
/|\ |
    |
    |
=====""",
r"""
 +--+
 |  |
 O  |
/|\ |
/   |
    |
=====""",
r"""
 +--+
 |  |
 O  |
/|\ |
/ \ |
    |
====="""]


CATEGORY = 'Animals'
WORDS = 'ANT BABOON BADGER BAT BEAR BEAVER CAMEL CAT CLAM COBRA COUGAR COYOTE CROW DEER DOG DONKEY DUCK EAGLE FERRET FOX FROG GOAT GOOSE HAWK LION LIZARD LLAMA MOLE MONKEY MOOSE MOUSE MULE NEWT OTTER OWL PANDA PARROT PIGEON PYTHON RABBIT RAM RAT RAVEN RHINO SALMON SEAL SHARK SHEEP SKUNK SLOTH SNAKE SPIDER STORK SWAN TIGER TOAD TROUT TURKEY TURTLE WEASEL WHALE WOLF WOMBAT ZEBRA'.split()

def main():
    missed_letters = "" #string of incorrect letter guesses.
    guessed_letters = "" #string of correct letter guesses
    secret_word = random.choice(WORDS)

    scalet_secret_word = ["_"] * len(secret_word) # infrastructure for secret word.
    print("Hangman, by Fatih Karahan sekanti02@gmail.com")
    while True: # Main game loop.
        draw_hangman(missed_letters, guessed_letters, secret_word, scalet_secret_word)

        guess = get_guess(missed_letters+guessed_letters)

        if guess in secret_word:
            guessed_letters += guess
            # Check whether player won after this correct one.
            if sorted(guessed_letters) == sorted(secret_word):
                print(f"Congratulations you won before the man hang, the secret word was {secret_word}")
                print("Thanks for playing.")
                break
        else:
            missed_letters += guess
            # Check whether player lost after this wrong guess.
            if len(missed_letters) == len(HANGMAN_PICS)-1:
                print(HANGMAN_PICS[-1])
                print(f"The man already hang, You lost. The secret word was {secret_word}")
                print("Thansk for playing")
                break


def draw_hangman(missed_letters, guessed_letters, secret_word, scalet_secret_word):
    """Draws the current situation of the game."""
    print("Category: ", CATEGORY)
    print(HANGMAN_PICS[len(missed_letters)])
    print("Missed letters:"," ".join(missed_letters))

    
    for i in range(len(secret_word)):
        if secret_word[i] in guessed_letters:
            scalet_secret_word[i] = secret_word[i]
    displayed_text = " ".join(scalet_secret_word)
    print(displayed_text)


def get_guess(total_guess):
    """Checks the taken guess is one letter and wasn't taken before."""
    while True:
        print("Guess a letter.")
        guess = input("> ").upper()
        if len(guess) != 1:
            print("Please type just one letter.")
        elif guess in total_guess:
            print("You have made this guess before. Please type another letter in.")
        elif not guess.isalpha():
            print("Please type a letter.")
        else:
            break
    return guess


if __name__ == "__main__":
    main()