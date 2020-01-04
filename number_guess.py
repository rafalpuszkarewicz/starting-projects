import random
import time


def solver(a, b):
    return (a + b) // 2


print("Welcome to the Guess the Number!")
# name = input("Enter your name: \n")
# print(f"{name}, I'm thinking about number between 1 and 100.")
a = 1
b = 1000
number = random.randint(a, b)
guesses = 0

while True:
    print("Take a guess.")
    guesses += 1

    guess = solver(a, b)
    time.sleep(1)
    print(guess)

    if guess > number:
        print("Too high.")
        b = guess
    elif guess < number:
        print("Too low.")
        a = guess
    else:
        print(f"Correct! You guessed in {guesses} guesses!")
        break

