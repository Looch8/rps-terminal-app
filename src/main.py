# ROCK PAPER SCISSORS

# Modules
import random  # for getting random computer choice
import csv  # for reading and writing scores to csv file
import sys  # provide info on functions
import unittest  # for testing

# Function imports

# # Create CSV file
# with open('score.csv', 'w') as csv_file:
#     fieldnames = ['Player', 'Computer', 'Score']
#     writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
#     writer.writeheader()

# Append player and computer information to CSV file
#  with open('score.csv', 'a') as csv.file:
#         writer = csv.writer(csv_file)
#         writer.writerow(['Player', player_score])
#         writer.writerow(['Computer', computer_score])

# Function to get player choice, will raise error if use does not enter either 'rock', 'paper', or 'scissors'. Input is not case sensitive

# Player choice


def get_player_choice():
    while True:
        player_choice = input(
            'Choose rock, paper, or scissors - or type "end" to exit: ').lower()
        if player_choice == "end":
            # had to use exit to exit program - break was not working, not sure why.
            print('Goodbye, thank you for playing!')
            exit()
        elif player_choice not in ['rock', 'paper', 'scissors']:
            # Raise value error if not an input from list
            raise ValueError('Not a valid choice')
        else:
            return player_choice
    # print('Goodbye, Thank you for playing!')
# Computer choice


def get_computer_choice():
    computer_choices = ['rock', 'paper', 'scissors']
    computer_choice = random.choice(computer_choices)
    return computer_choice

# Round of RPS


def play_round(player_choice, computer_choice):
    if player_choice == computer_choice:
        return ('draw')
    elif player_choice == 'rock' and computer_choice == 'scissors' or player_choice == 'paper' and computer_choice == 'rock' or player_choice == 'scissors' and computer_choice == 'paper':
        return 'player'
    else:
        return 'computer'
# Save score to CSV file


def save_scores(player_score, computer_score):
    with open('scores.csv', 'a') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow([player_score, computer_score])

# Print scores


def print_scores():
    with open('scores.csv', 'r') as csv_file:
        reader = csv.reader(csv_file)
        player_wins = 0
        computer_wins = 0
        for row in reader:
            player_wins = int(row[0])
            computer_wins = int(row[1])
        print(f'Player score: {player_wins}')
        print(f'Computer score: {computer_wins}')


def game():
    # Initial scores
    player_score = 0
    computer_score = 0
    while True:
        player_choice = get_player_choice()
        computer_choice = get_computer_choice()
        winner = play_round(player_choice, computer_choice)
        if winner == 'draw':
            print(f"It's a draw, you both picked {player_choice}")
        elif winner == 'player':
            player_score += 1
            print(f"You win - {player_choice} beats {computer_choice}")
        else:
            computer_score += 1
            print(f"You lose - {computer_choice} beats {player_choice}")
        save_scores(player_score, computer_score)
        print_scores()

        # End game
        if player_score == 5:
            print('Game over - You win!')
            break
        elif computer_score == 5:
            print('Game over - Computer wins!')
            break


    # # Loop number of rounds
    # for current_round in range(1, 6):
    #     print(f'Round {current_round}')
    #     play_round(player_choice='rock', computer_choice='scissors')
    #     current_round += 1
game()


def reset_game():
    pass


# User choice
# player_selection = input('rock, paper, or scissors? ').lower()


# # calling comp function to randomize computer choice
# computer_selection = get_computer_choice()
# print(play_round(get_player_choice, computer_selection))

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
