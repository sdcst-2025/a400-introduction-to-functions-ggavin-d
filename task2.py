"""
Create a program to play a number guessing game
There should be a function:
title()
displays instructions and how to play

game()
plays the game

This will be silimar to something you have already done, but in this task you 
are breaking the code up into different sections to make each a function.
"""
import random

def title():
    print("How To Play: Pick a number between 1 - 5, you recieve only one try")


def game():
    ans = random.randint(1 , 5)
    print(ans)
    player = int(input('enter a number'))
    if player == ans:
        print("you guessed right!")
    else:
        print("wrong number, better luck next time!")


while True:
    x = input('Welcome to "The Game"! enter "Help" to view the rules, enter "Play" to get right in | ')
    if x == "Help":
       title()
    elif x == "Play":
        game()