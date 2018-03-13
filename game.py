def game (JugadorA, JugadorB):
    """
    Enter the values that represent the player choice
    Return pl if player 1 wins otherway p2
    """


    if JugadorA == 'rock' and JugadorB == 'scissors' :
            return 'rock WINS'

    elif JugadorA == 'rock' and JugadorB == 'paper' :
            return 'paper WINS'

    elif JugadorA == 'paper' and JugadorB == 'scissors' :
            return 'scissors WINS'

    elif JugadorA == 'paper' and JugadorB == 'rock' :
            return 'paper WINS'

    else: 
            print 'Empate'

