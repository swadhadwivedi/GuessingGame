import random

def guess(x):
    random_number = random.randint(1,x)
    guess = 0
    while guess != random_number:
        guess = int(input(f'Enter a random number between 1 and {x}:'))
        if guess < random_number:
            print ('Too low love, try again!')
        elif guess > random_number:
            print ('Too high love, try again!')
    print ('Congrats boo! You have got it.')

guess(10)
