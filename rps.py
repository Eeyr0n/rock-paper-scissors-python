
import random
import time
import sys

moves = ['r', 'p', 's']
wins = 0
losses = 0
ties = 0

print('Welcome to ROCK, PAPER, SCISSORS')

def scoreboard():
    print('WINS: ' + str(wins) + '    LOSSES: ' + str(losses) + '    TIES: ' + str(ties))
    
def getPlayerMove():
    global playerMove
    playerMove = ''
    while playerMove != 'r' or playerMove != 'p' or playerMove != 's':
        print('Enter your move(r/p/s)')
        playerMove = input()
        if playerMove == 'r' or playerMove == 'p' or playerMove == 's':
            break

def whatIsPlayerMove():
    if playerMove == 'r':
        print('Rock VERSUS...')
    if playerMove == 'p':
        print('Paper VERSUS...')
    if playerMove == 's':
        print('Scissors VERSUS...')
        
def getComputerMove():
    computerMove = moves[random.randint(0, len(moves) - 1)]
    if computerMove == 'r':
        print('Rock')
    if computerMove == 'p':
        print('Paper')
    if computerMove == 's':
        print('Scissors')
        
def didPlayerWin():
    global wins
    global losses
    global ties
    if playerMove == computerMove:
        print('It\'s a tie')
        ties += 1
    if playerMove == 'r' and computerMove == 'p':
        print('You lose')
        losses += 1
    if playerMove == 'r' and computerMove == 's':
        print('You win')
        wins += 1
    if playerMove == 'p' and computerMove == 's':
        print('You lose')
        losses += 1
    if playerMove == 'p' and computerMove == 'r':
        print('You win')
        wins += 1
    if playerMove == 's' and computerMove == 'r':
        print('You lose')
        losses += 1
    if playerMove == 's' and computerMove == 'p':
        print('You win')
        wins += 1

def playAgain():
    answer = ''
    while answer != 'y' or answer != 'n':
        print('Would you like to play again?')
        answer = input()
        if answer == 'y':
            scoreboard()
            getPlayerMove()
            whatIsPlayerMove()
            getComputerMove()
            didPlayerWin()
            playAgain()
        elif answer == 'n':
            scoreboard()
            sys.exit()


scoreboard()
getPlayerMove()
whatIsPlayerMove()
getComputerMove()
didPlayerWin()
playAgain()