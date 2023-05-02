import pytest  # for testing
from main import play_round, get_computer_choice


# Test the play_round function


def test_play_round():
    # Player wins - This tests whether the play_round() function returns 'player' when the player wins.
    assert play_round('rock', 'scissors') == 'player'
    assert play_round('paper', 'rock') == 'player'
    assert play_round('scissors', 'paper') == 'player'

    # Computer wins - This tests whether the play_round() function returns 'computer' when the computer wins.
    assert play_round('rock', 'paper') == 'computer'
    assert play_round('paper', 'scissors') == 'computer'
    assert play_round('scissors', 'rock') == 'computer'

    # draw - This tests whether the play_round() function returns 'draw' when both the player and the computer choose the same option
    assert play_round('rock', 'rock') == 'draw'
    assert play_round('paper', 'paper') == 'draw'
    assert play_round('scissors', 'scissors') == 'draw'

# Test the get_player_choice function


# Test the get_computer_choice function - using monkeypatch to replace random.choice function and with a lambda function to always return a predefined string.
def test_get_computer_choice(monkeypatch):
    # Test case 1: simulate the computer choosing 'rock'
    monkeypatch.setattr('random.choice', lambda x: 'rock')
    assert get_computer_choice() == 'rock'

    # Test case 2: simulate the computer choosing 'paper'
    monkeypatch.setattr('random.choice', lambda x: 'paper')
    assert get_computer_choice() == 'paper'

    # Test case 3: simulate the computer choosing 'scissors'
    monkeypatch.setattr('random.choice', lambda x: 'scissors')
    assert get_computer_choice() == 'scissors'
