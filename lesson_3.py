#COMPARE TWO NUMBERS
# a = input("Enter the first number: ")
# b = input("Enter the second number: ")
#
#
# if a < b:
#     print(f"The greater number is {b}")
# elif a > b:
#     print(f"The greater number is {a}")
# else:
#     print("Numbers are equal")


#CASINO AGE CHECK
# name1 = input("Enter your name: ")
# name2 = input("Enter your surname: ")
# age = int(input("Enter your age: "))
#
# if age >= 21:
#     print(f"{name1} {name2}, you are allowed to enter the casino.")
# else:
#     print("You need to wait a few years.")


#SMALL CALCULATOR APPLICATION
# a = input("Enter the first number: ")
# s = input("Enter the symbol (+, -, *, /): ")
# b = input("Enter the second number: ")
#
# a = float(a)
# b = float(b)
#
# if s == "+":
#     print(f"The result of {a} {s} {b} is", a + b)
# elif s == "-":
#     print(f"The result of {a} {s} {b} is", a - b)
# elif s == "*":
#     print(f"The result of {a} {s} {b} is", a * b)
# elif s == "/":
#     print(f"The result of {a} {s} {b} is", a / b)
# else:
#     print("WOT R U DOIN?")



#LIBRARY BOOK LOAN ELIGIBILITY
# member = input("Are you library member? (yes/no): ")
#
# if member == "yes":
#     age = int(input("Enter your age: "))
#     if age >= 12:
#         print("You can loan all books.")
#
#     elif member == "yes" and age < 12:
#         adult = input("Is an adult accompanying you? (yes/no): ")
#         if adult == "no":
#             print("You can only loan children's books.")
#         else:
#             print("You can loan all books.")
# else:
#     print("You cannot loan any books.")



#NUMBER GUESSING GAME
import random

a = int(input("Guess the number (0-10): "))
b = random.randint(0, 10)

while a != b:
    if a < b:
        print("Too low! Try again.")
        a = int(input("Another guess: "))
    elif a > b:
        print("Too high! Try another one.")
        a = int(input("Another guess: "))
else:
    print("Yes!")