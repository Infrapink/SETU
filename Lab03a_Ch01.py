#!/usr/bin/python3

# Guessing game

import random

def get_secret_number():
    """Generate a random integer between 1 and 100 inclusive"""
    return random.randint(1,100)

def get_guess():
    """User inputs their guess"""
    return int(input("Guess the number (1 — 100): "))

def check_guess(secret, guess):
    """Check if the user got it right"""
    if (secret == guess):
        print("That's right!")
        return True
    elif (secret > guess):
        print("Too low")
    else:
        print("Too high")
    return False

# main programme
def game():
    """The main game loop"""
    correct = False
    ans = get_secret_number()
    tries = 0
    while (not(correct)):
        tries += 1
        guess = get_guess()
        correct = check_guess(ans, guess)
    print(f"You got it in {tries} attempts!")

game()