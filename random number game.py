import random


def gamble():
    global guess
    guess = 0
    random_number = random.randint(1, 11)
    guess = int(input("What do you guess: "))
    while guess == random_number is False:
        if guess == random_number:
            print(f"correct! it was {random_number}")
        else:
            if guess > random_number:
                print("wrong! it is less")
            else:
                print("wrong! it is more")



gamble()