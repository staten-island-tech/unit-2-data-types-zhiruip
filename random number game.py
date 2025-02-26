import random


def gamble():
    global guess
    guess = 0
    random_number = random.randint(1, 11)
    guess = int("What do you guess: ")
    while guess != random_number:
        if guess == random_number:
            print(f"correct! it was {random_number}")
        else:
            if guess > random_number:
                input("wrong! it is less, guess again: ")
            else:
                input("wrong! it is more, guess again: ")



gamble()