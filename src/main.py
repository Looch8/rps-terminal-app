# ROCK PAPER SCISSORS

# Modules
import random  # for getting random computer choice
import csv  # for reading and writing scores to csv file
import sys  # provide info on functions
import unittest  # for testing


# Function that generates a computer choice


def get_computer_choice():
    # Random int between 0, 1, 2
    num = random.randint(0, 2)
    if num == 0:
        return 'rock'
    elif num == 1:
        return 'paper'
    else:
        return 'scissors'

# Function that gets user input

# Function that plays one round of RPS.


def play_round(player_selection, computer_selection):
    if player_selection == computer_selection:
        return (f"It's a draw, you both picked {player_selection}")
    elif player_selection == 'rock' and computer_selection == 'scissors' or player_selection == 'paper' and computer_selection == 'rock' or player_selection == 'scissors' and computer_selection == 'paper':
        return (f'You win, {player_selection} beats {computer_selection}!')
    else:
        return (f'You lose, {computer_selection} beats {player_selection}')


def player_choice(player_selection):
    while player_selection != 'rock' or player_selection != 'paper' or player_selection != 'scissors':
        return player_selection


player_selection = input('rock, paper, or scissors? ').lower()

# calling comp function to randomize computer choice
computer_selection = get_computer_choice()
print(play_round(player_selection, computer_selection))

# Function that keeps score (first to 5 wins) and prints winner to the console
# Ability to reset game at any point in time during the game
# Function to reset game and start again once a winner is announced
# score function in file that updates with each round (thanks for suggestion, Simon)


# Hardware requirements just has to be "what hardware you tested it on"

# for best marks, must use 4+ imported packages (csv, colored, etc)
#   N.B. this does NOT include importing your own functions. You need 5 of these as well.

# Include a script file to run application, like we did in Week 8 Day 3 class (around 2.5 hours in iirc)

# MULTIPLE bash scripts required. Suggested: one to check python, one to check packages, one to check all files available, one to run the program

# MINIMUM 20 commits. Will only get 2/6 marks if you have less than 20. Cannot be all in one day (RIP procrastina

# A couple of my notes:
# Project management platforms: trello, monday.com, meistertask
# Testing: can be automatic (using pytest for example) or manual (using a spreadsheet)
