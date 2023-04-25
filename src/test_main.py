import pytest  # for testing
from unittest import mock
from main import play_round


# @mock.patch('main.play_round', return_value='rock', autospec=True)
# def test_play_round(mock_play_round):
#     assert play_round('scissors') == 'player'

# def test_play_round(monkeypatch):
#     monkeypatch.setattr('builtins.input', lambda _: 'rock')
#     assert play_round()
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

def test_play_round():
    # Player wins
    assert play_round('rock', 'scissors') == 'player'
    assert play_round('paper', 'rock') == 'player'
    assert play_round('scissors', 'paper') == 'player'

    # Computer wins
    assert play_round('rock', 'paper') == 'computer'
    assert play_round('paper', 'scissors') == 'computer'
    assert play_round('scissors', 'rock') == 'computer'

    # draw
    assert play_round('rock', 'rock') == 'draw'
    assert play_round('paper', 'paper') == 'draw'
    assert play_round('scissors', 'scissors') == 'draw'
