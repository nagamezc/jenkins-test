from game import game

def test_game_01():
    assert game('rock', 'scissors') == 'rock WINS', 'rock should win'
    assert game('rock', 'paper') == 'paper WINS', 'paper should win'
    assert game('paper', 'scissors') == 'scissors WINS', 'scissors should win'
    assert game('paper', 'rock') == 'paper WINS', 'paper should win'
