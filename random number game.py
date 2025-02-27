import random  # Make sure to import random module

def gamble(min_value, max_value):
    return random.randint(min_value, max_value)

random_number = gamble(1, 11)

while True:
    x = int(input("Guess a number between 1 and 11: "))
    if x == random_number:
        print("correct") 
    break
    elif x > random_number:
           print("more")
    else:
  print("less")

