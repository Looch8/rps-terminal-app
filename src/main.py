# ROCK PAPER SCISSORS

# Modules
import random  # for getting random computer choice
import csv  # for reading and writing scores to csv file
from colored import fg, bg, attr
from art import tprint
import emoji

# Intro message
tprint('Rock Paper Scissors!')


def get_player_choice():
    while True:
        try:
            player_choice = input(
                f"\n{fg('yellow')}Choose rock 🪨  paper ''📄 o''scisso ✂️'' - or type 'end' to quit: \n\n").lower()
            if player_choice == "end":
                print(emoji.emojize(
                    f'\n{fg(5)}Goodbye, thank you for playing! 😊', language='alias'))
                exit()
            elif player_choice not in ['rock', 'paper', 'scissors']:
                raise ValueError
            else:
                return player_choice
        except ValueError as e:
            print(f'{fg(28)} {e} is not a valid choice, please choose again.')


def get_computer_choice():
    try:
        computer_choices = ['rock', 'paper', 'scissors']
        computer_choice = random.choice(computer_choices)
        return computer_choice
    except IndexError:
        print('Element not present in list, or list is empty.')
        return None
    except Exception as e:
        print(f'An error occurred: {e}')
        return None


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
    try:
        with open('scores.csv', 'a') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow([player_score, computer_score])
    except OSError as e:
        print(f'Error writing scores to csv file: {e}')

# Print scores


def print_scores():
    try:
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
    except ValueError:
        print('There was an error reading the scores file.')
    except FileNotFoundError:
        print('The scores file was unable to be found.')


def game():
    try:
        # Initial scores
        player_score = 0
        computer_score = 0
        while True:
            player_choice = get_player_choice()
            computer_choice = get_computer_choice()
            winner = play_round(player_choice, computer_choice)
            if winner == 'draw':
                print(
                    f"\n{fg(28)}YOU DREW! - you both picked {player_choice}! {attr('reset')}😮")
            elif winner == 'player':
                player_score += 1
                print(
                    f"\n{fg(21)} YOU WIN! - {player_choice} beats {computer_choice}! {attr('reset')}😀")
            else:
                computer_score += 1
                print(
                    f"\n{fg(9)}YOU LOSE! - {computer_choice} beats {player_choice}! {attr('reset')}🙁")
            save_scores(player_score, computer_score)
            print_scores()

            # End game
            if player_score == 5:
                print(f'\n{bg("blue")}Game over - YOU WON!🏆')
                break
            elif computer_score == 5:
                print(f'\n{bg("red")}Game over - COMPUTER WON!😭')
                break
    except KeyboardInterrupt:
        print('Game interrupted by player')
    except Exception as e:
        print(f'an error occurred during the game: {e}')


# To prevent entire script from running when testing
if __name__ == "__main__":
    game()

# Hardware requirements just has to be "what hardware you tested it on"

#   N.B. this does NOT include importing your own functions. You need 5 of these as well.


# Project management platforms: trello, monday.com, meistertask
