# Modules
import random  # for getting random computer choice

# Function to get player choice, will raise error if use does not enter either 'rock', 'paper', or 'scissors'. Input is not case sensitive

# Player choice


def get_player_choice():
    while True:
        player_choice = input('rock, paper, or scissors?: ').lower()
        if player_choice not in ['rock', 'paper', 'scissors']:
            # Raise value error if not an input from list
            raise ValueError('Not a valid choice')
        else:
            return player_choice

# Computer choice


def get_computer_choice():
    computer_choices = ['rock', 'paper', 'scissors']
    computer_choice = random.choice(computer_choices)
    return computer_choice

# Round of RPS


def play_round(player_choice, computer_choice):
    if player_choice == computer_choice:
        return ('Draw!')
    elif player_choice == 'rock' and computer_choice == 'scissors' or player_choice == 'paper' and computer_choice == 'rock' or player_choice == 'scissors' and computer_choice == 'paper':
        return f'You win - {player_choice} beats {computer_choice}!'
    else:
        return f'You lose = {computer_choice} beats {player_choice}!'
