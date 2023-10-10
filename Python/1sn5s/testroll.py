from analyticalutilities import *
from onesandfives import Turn
import random
import json
import numpy

def roll(n,seed):
        if n == 0:
            n=6
        #roll n dice
        rolllookup = getrolllookup()
        possibilities = rolllookup[n-1]


        #randomindex = random.randint(1,(6**n))
        randomindex=seed+1
        cumulativeindex=0
        for possibility in possibilities:
            roll = possibility[0]
            frequency = possibility[1]
            cumulativeindex+=frequency

            
            if cumulativeindex>=randomindex:
                print(randomindex,roll)
                break
for i in range(6):
    roll(1,i)
