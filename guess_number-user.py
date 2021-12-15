import random

def guess(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'c':
        guess = random.randint(low, high)
        feedback = input(f"is {guess} too high (H), too low (L) or correct (C)? "). lower
        if feedback == "H":
            high = 1 - guess
        elif feedback == "L":
            low = 1 + guess
    print("You guessed it corrrect")