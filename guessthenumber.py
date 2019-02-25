#!/usr/bin/env python3

import random

number = random.randint(1, 10)
tries = 0
score = 0

uname = input("Hello! What is your name? ")

print("Hello", uname + ".", )

question = input("Would you like to play a game? [Y/N] ")
if question != "y":
    while question != "y":
        print("Oh..okay.")
        question = input("Would you like to play a game now? [Y/N] ")
if question == "y":
    print("We will play for 3 rounds. Try to get a perfect score of 30!")
    print("I'm thinking of a number between 1 and 10.")
    guess = int(input("Have a guess: "))
    if guess != number:
        while guess != number:
            tries += 1
            score -= 1
            if guess > 10:
                print(guess, "is not between 1 and 10.")
            if guess < 1:
                print(guess, "is not between 1 and 10.")
            if guess > number:
                if guess < 10:
                    print("Guess lower...")
            if guess < number:
                if guess > 1:
                    print("Guess higher...")
            guess = int(input("Try again: "))
    if guess == number:
        tries += 1
        score += 10
        print("You're right! The number was", number, "and it only took", tries, "tries! Your score is", score)

# Round 2
tries = 0
number2 = random.randint(1, 10)

print("I'm thinking of a number between 1 and 10.")
guess = int(input("Have a guess: "))
if guess != number2:
    while guess != number2:
        tries += 1
        score -= 1
        if guess > 10:
            print(guess, "is not between 1 and 10.")
        if guess < 1:
            print(guess, "is not between 1 and 10.")
        if guess > number2:
            print("Guess lower...")
        if guess < number2:
            print("Guess higher...")
        guess = int(input("Try again: "))
if guess == number2:
    tries += 1
    score += 10
    print("You're right! The number was", number2, "and it only took", tries, "tries! Your score is", score)

# Round 3
tries = 0
number3 = random.randint(1, 10)

print("I'm thinking of a number between 1 and 10.")
guess = int(input("Have a guess: "))
if guess != number3:
    while guess != number3:
        tries += 1
        score -= 1
        if guess > 10:
            print(guess, "is not between 1 and 10.")
        if guess < 1:
            print(guess, "is not between 1 and 10.")
        if guess > number3:
            print("Guess lower...")
        if guess < number3:
            print("Guess higher...")
        guess = int(input("Try again: "))
if guess == number3:
    tries += 1
    score += 10
    print("You're right! The number was", number3, "and it only took", tries, "tries! Your final score is", score)