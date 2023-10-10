from analyticalutilities import *
from onesandfives import Turn
import random

reasonableclaimlookup = getreasonableclaimlookup()


def bankingdecision(turn): ##These are the two things you need to teach it how to do
    tempscore = turn.getScore()
    dice = turn.getDice()
    numberofdice = len(dice)
    
    if random.random()>0.9:
        print("banking ",turn.bank())
        return True
    else:
        turn.roll(numberofdice)
        turn.dead = turn.checkIfDead()
        print("rolled ", turn.getDice())
        return False
def scoringdecision(turn): ##This too
    tempscore = turn.getScore()
    dice = turn.getDice()
    numberofdice = len(dice)
    reasonableclaims = reasonableclaimlookup[str(dice)]

    numberofreasonableclaims=len(reasonableclaims)
    randomclaimindex = random.randint(0,numberofreasonableclaims-1)
    turn.score+=reasonableclaims[randomclaimindex][1]
    turn.dice = ["x"]*(numberofdice-reasonableclaims[randomclaimindex][0])
    print("Scored ", reasonableclaims[randomclaimindex][1])                   




def playround():
    turn = Turn()
    print("rolled ", turn.getDice())
    finished = False
    while not(finished):
        if not turn.dead:
            scoringdecision(turn)
            finished = bankingdecision(turn)
        else:
            finished = True
    if turn.dead:
        print("Game over with 0 points.")
    else:
        print("Game over with ", turn.getScore()," points.")
        
        
playround()


    
