import csv
import random

# Valid choices
valid_choices = ['rock', 'paper', 'scissors']


def get_player_choice():
    while True:
        player_selection = input('rock, paper, or scissors? ').lower()
        if player_selection not in valid_choices:
            raise ValueError('Invalid choice')
        else:
            return player_selection


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


def update_score(winner):
    with open("score.csv", "r") as file:
        reader = csv.reader(file)
        score = next(reader)
        if winner == "user":
            score[0] = str(int(score[0]) + 1)
        elif winner == "computer":
            score[1] = str(int(score[1]) + 1)
    with open("score.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(score)
