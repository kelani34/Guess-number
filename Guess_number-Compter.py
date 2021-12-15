import random
def guess(x, level):
    if x > 0:
        random_num = random.randint(1, x)
        guess = 0
        if level == 'e':
            level += 10 
        else:
            level += 5
        while guess != random_num and level != 0:
            guess = int(input(f"Guess a number between 1 and {x} a number: "))
            if guess > random_num:
                print("too high")
            elif guess < random_num:
                print("too low")
            level -= 1
    print(f"you guessed the random number {random_num} correct")
user_level = input("Which level do you wnat to choose. 'H' for HARD LEVEL 'E' for EASy level: ").lower
user_input = int(input("Enter a number:"))
guess(user_input, user_level)
