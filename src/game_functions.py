# Modules
import random  # for getting random computer choice

# Function to get player choice, will raise error if use does not enter either 'rock', 'paper', or 'scissors'. Input is not case sensitive


def get_player_choice():
    while True:
        player_choice = input('rock, paper, or scissors?: ').lower()
        if player_choice not in ['rock', 'paper', 'scissors']:
            raise ValueError('Not a valid choice')
        else:
            return player_choice


def get_computer_choice():
    computer_choices = ['rock', 'paper', 'scissors']
    computer_choice = random.choice(computer_choices)
    return computer_choice
