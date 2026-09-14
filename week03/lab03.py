import random


def generate_mad_lib(adjective, noun, verb):
    """Return a nonempty story containing all three supplied words."""
    story = f"The {adjective} {noun} suddenly {verb} across the room."
    return story


def guessing_game():
    """Run an interactive number-guessing game."""
    secret_number = random.randint(1, 100)

    while True:
        guess = int(input("Guess a number between 1 and 100: "))

        if guess < secret_number:
            print("Too low!")
        elif guess > secret_number:
            print("Too high!")
        else:
            print("Correct! You guessed the number!")
            break