import random
from collections import Counter
class Turn:
    
    def __init__(self, scripteddice=[]):
        self.score=0
        self.currentSubturn=None
        if scripteddice==[]:
            self.dice=self.roll(6)
        else:
            self.dice=scripteddice

        self.dead=self.checkIfDead()
        self.hasClaimedSomething=False

    def fixLists(self,dicetoclaim,i,n):
        for j in range(n):
            dicetoclaim.remove(i)
            self.dice.remove(i)
        
        
    def roll(self,n):            #roll n dice
        return random.choices([1,2,3,4,5,6], k=n)

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



    def claim(self,dicetoclaim):      
            #code that scores whatever list you enter
            #and then scores and removes dice
            if not(Counter(dicetoclaim)<=Counter(self.dice)):#check we are claiming subset of rolled dice
                raise Exception("Naughty Naughty, you don't have that")
            
            
            counter=Counter(dicetoclaim)#convert to frequencies
            frequencies=[counter[x] for x in [1,2,3,4,5,6]]

            
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
                                                
                if dicetoclaim!=[]:
                    raise Exception("stop claiming garbage")
                
    def getDice(self):
        return sorted(self.dice)

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
    




        

##class Strategy:
##    def __init__(self):
##        hasclaimed=False




t=Turn()
while True: #begins with 6 dice rolled
    
    if t.checkIfDead(): #Check if we lost
        print("You rolled "+ str(t.getDice())+". Bad luck!")
        break

    print("Score: "+str(t.getScore()))
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
    



        
##    if (strategy says so):
##        roll+claim
##    else:
##        bank
##        quit
##
##print score
