import random
from collections import Counter
from analyticalutilities import *
class Turn:
    
    def __init__(self, scripteddice=[], allowerrors=False):
        self.score=0
        if scripteddice==[]:
            self.dice=self.roll(6)
        else:
            self.dice=scripteddice
        self.allowerrors=allowerrors
        self.dead=self.checkIfDead()
        self.hasClaimedSomething=False

    def fixLists(self,dicetoclaim,i,n):
        for j in range(n):
            #dicetoclaim.remove(i)
            self.dice.remove(i)
        
        
    def roll(self,n):
        if n == 0:
            n=6
        #roll n dice
        rolllookup = getrolllookup()
        possibilities = rolllookup[n-1]

        randomindex = random.randint(1,(6**n))
        cumulativeindex=0
        for possibility in possibilities:
            roll = possibility[0]
            frequency = possibility[1]
            cumulativeindex+=frequency

            
            if cumulativeindex>=randomindex:
                self.dice=roll
                return roll

            
            
        #return random.choices([1,2,3,4,5,6], k=n)

    def checkIfDead(self):
        counter=Counter(self.dice) #convert to dice frequencies
        frequencies=[counter[x] for x in [1,2,3,4,5,6]]

        if frequencies==[1,1,1,1,1,1]:#check 123456
            return False     
        if any(frequencies[i-1]>=3 for i in range(1,7)):
            return False
        if (frequencies[0]>=1 or frequencies[4]>=1):#check 1s or 5s
            return False
        else:
            return True



    def claim(self,dicetoclaim,cleverclaim=False):      
            #code that scores whatever list you enter
            #and then scores and removes dice
            if not(Counter(dicetoclaim)<=Counter(self.dice)):#check we are claiming subset of rolled dice
                raise Exception("Naughty Naughty, you don't have that")
            
            
            counter=Counter(dicetoclaim)#convert to frequencies
            frequencies=[counter[x] for x in [1,2,3,4,5,6]]

            if cleverclaim:
                rememberscore=self.score
                rememberdice=len(self.dice)
    
            
            if frequencies==[1,1,1,1,1,1]:#123456
                self.score+=2000
                self.dice=[]
                self.hasClaimedSomething=True
            else:
                for i in range(1,7):
                    if frequencies[i-1]>=3: #if there is a set of >=3
                        if i==1:
                            basescore=1000
                        else:
                            basescore=100*(i)
                        self.score+=basescore*2**(frequencies[i-1]-3)
                        self.fixLists(dicetoclaim,i,frequencies[i-1])
                        self.hasClaimedSomething=True

                    else:
                        if i==1:
                            self.score+=100*frequencies[i-1]
                            self.fixLists(dicetoclaim,i,frequencies[i-1])
                            self.hasClaimedSomething=True
                        if i==5:
                            self.score+=50*frequencies[i-1]
                            self.fixLists(dicetoclaim,i,frequencies[i-1])
                            self.hasClaimedSomething=True

                if cleverclaim:
                    if (rememberdice>4 and self.score-rememberscore<300):
                        if frequencies[0]>0:
                            self.dice=[0]*(rememberdice-1)
                            self.score=rememberscore+100
                            #print("I did something")
                        elif frequencies[4]>0:
                            self.dice=[0]*(rememberdice-1)
                            self.score=rememberscore+50
                            #print("I did something")
                        else:
                            pass
                                                
                if (dicetoclaim!=[] and not self.allowerrors):
                    raise Exception("stop claiming garbage")
                
    def getDice(self):
        return (self.dice)

    def getScore(self):
        return self.score

    #during a turn, you play a subturn, roll, play a subturn, roll
    #,..., bank/die



    def reroll(self):
        #somewhere must check if scored something
        if not(self.dead):
            if self.dice!=[]:
                self.dice=self.roll(len(self.dice))
            else:
                self.dice=self.roll(6)
        else:
            raise Exception("You're dead, you cannot roll")
            

    def bank(self):
        return self.score
        #and kill the class instance?
    




        





    



        
##    if (strategy says so):
##        roll+claim
##    else:
##        bank
##        quit
##
##print score
