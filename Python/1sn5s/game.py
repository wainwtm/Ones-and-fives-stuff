import random
from collections import Counter
from onesandfives import Turn
t=Turn()
while True: #begins with 6 dice rolled
    
    if t.checkIfDead(): #Check if we lost
        print("You rolled "+ str(t.getDice())+". Bad luck!")
        break

    print("Score: "+str(t.getScore()))

    # strategy.getclaim(currentscore, currentdice)
    claimstring=input("You rolled "+ str(t.getDice())+". What would you like to claim?  ")
    claimlist=[int(x) for x in claimstring]
    t.claim(claimlist) #claims dice input by user

    if t.getScore()>349: #banking becomes available at 350
        print("Score: "+str(t.getScore()))

        bankchoice=input("Bank?? y/n  ")
        if bankchoice=="y":
            t.bank()#this function dosen't do much yet
            print("Turn over at "+str(t.getScore())+" points")
            break
            

    t.reroll() #roll remaining dice and repeat
