# ROCK PAPER SCISSORS

# Modules
import random  # for getting random computer choice
import csv  # for reading and writing scores to csv file
from colored import fg, bg, attr
import sys  # provide info on functions


def get_player_choice():
    while True:
        try:
            player_choice = input(
                f"\n{fg('yellow')}Type 'rock', 'paper', or 'scissors' - or type 'end' to quit: ").lower()
            if player_choice == "end":
                print(f'\n{fg(5)}Goodbye, thank you for playing! :)')
                exit()
            elif player_choice not in ['rock', 'paper', 'scissors']:
                raise ValueError
            else:
                return player_choice
        except ValueError as e:
            print(f'{fg(28)}Not a valid choice, please choose again.')


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
        print(
            f"{fg(15)} {bg('blue')}Player score: {player_wins} {attr('reset')}")
        print(
            f"{fg(15)} {bg('red')}Computer score: {computer_wins} {attr('reset')}")


def game():
    # Initial scores
    player_score = 0
    computer_score = 0
    while True:
        player_choice = get_player_choice()
        computer_choice = get_computer_choice()
        winner = play_round(player_choice, computer_choice)
        if winner == 'draw':
            print(
                f"\n{fg(28)}YOU DREW! - you both picked {player_choice}! {attr('reset')}")
        elif winner == 'player':
            player_score += 1
            print(
                f"\n{fg(21)} YOU WIN! - {player_choice} beats {computer_choice}! {attr('reset')}")
        else:
            computer_score += 1
            print(
                f"\n{fg(9)}YOU LOSE! - {computer_choice} beats {player_choice}! {attr('reset')}")
        save_scores(player_score, computer_score)
        print_scores()

        # End game
        if player_score == 5:
            print(f'\n{bg("blue")}Game over - YOU WON!')
            break
        elif computer_score == 5:
            print(f'\n{bg("red")}Game over - COMPUTER WON!')
            break


game()


def reset_game():
    pass


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
