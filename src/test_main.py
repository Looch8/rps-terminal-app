import pytest  # for testing
from main import play_round


def test_play_round(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: 'rock')
    assert play_round()
# Play_round function testing
# def test_play_round(monkeypatch):
#     # Player wins
#     assert play_round('rock', 'scissors') == 'player'
    # assert play_round('paper', 'rock') == 'player'
    # assert play_round('scissors', 'paper') == 'player'

    # # Computer wins
    # assert play_round('rock', 'paper') == 'computer'
    # assert play_round('paper', 'scissors') == 'computer'
    # assert play_round('scissors', 'rock') == 'computer'

    # # draw
    # assert play_round('rock', 'rock') == 'draw'
    # assert play_round('paper', 'paper') == 'draw'
    # assert play_round('scissors', 'scissors') == 'draw'
