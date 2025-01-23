import random
from random import randint
guess = input(f"Enter number from 1 to 99: ")
c = 1
number = randint(1,99)
while guess != "exit":
    if int(guess) == number:
        print(f"Yes! It was {number}")
        print(f"Number of guesses: {c}")
        guess = input(f"Enter number from 1 to 99: ")
        number = randint(1, 99)
        c = 1


    elif int(guess) > number:
        guess = input("Your number is too big, try smaller: ")
        c += 1
    elif int(guess) < number:
        guess = input("Your number is to small, try bigger: ")
        c += 1