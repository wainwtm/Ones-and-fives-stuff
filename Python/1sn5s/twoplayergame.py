from analyticalutilities import *
import numpy
import time

def setwins(database):
    for i in range(20):
        for j in range(20):
            if 50*(i+j)>=1000:
                database[i,:,:,j]=1





lookuptable=getrolllookup()#returns all unique dice rolls with 1,2,3,4,5,6 dice - precalculated


def bankingwinprob(playerscore,opponentscore,numberofdice,tempscore,lookup=False):

    if playerscore+tempscore>=1000:#this has to be done or items can be out of bounds on the winprobdatabase
        winprob=1
        
    elif lookup: #use value from the database
        winprob=winprobdatabase[int(playerscore/50),int(opponentscore/50),numberofdice-1,int(tempscore/50)]
        
    else: #if not lookup, calculate
        
        if tempscore==0: #if score is zero, banking is not an option
            sumofprobabilities=0 #used to hold the contribution to win prob. from all unique rolls
            for roll in lookuptable[numberofdice-1]:#iterates through all unique rolls with 'numberofdice' dice
                rollfrequency=roll[1]
                rolldice=roll[0]
                
                #find the prob of winning after rolling the roll
                rollwinprob=scoringwinprob(playerscore,opponentscore,numberofdice,tempscore,rolldice)
                
                sumofprobabilities+=rollfrequency*rollwinprob #this is a weighted sum
                
            winprob=sumofprobabilities/(6**numberofdice) #idk i think dividing by 6^n is better to do once than lots of times?

        else:
            bankwinprob=1-bankingwinprob(opponentscore,playerscore+tempscore,6,0,True)#prob of winning by banking is equal to
            #(1-opponent's prob to win vs your new score), True signals to use a lookup
            
            sumofprobabilities=0 #same code as before
            for roll in lookuptable[numberofdice-1]:
                rollfrequency=roll[1]
                rolldice=roll[0]
                rollwinprob=scoringwinprob(playerscore,opponentscore,numberofdice,tempscore,rolldice)
                sumofprobabilities+=rollfrequency*rollwinprob


            rollwinprob=sumofprobabilities/(6**numberofdice)
            
            winprob=max(bankwinprob,rollwinprob)#now must find max of
            #prob from banking, or expected prob from rolling
    return winprob



def scoringwinprob(playerscore,opponentscore,numberofdice,tempscore,roll):


    legalclaims=legalclaimslookup[str(roll)]#a legal claim is a scoring option
    
    #performance saver: if you can claim all dice, do
    for legalclaim in legalclaims:
        if len(legalclaim)==numberofdice:
            legalclaims=[legalclaim]
    
    if legalclaims!=[]: #if you didn't lose the round
        bankingprobs=[]
        for legalclaim in legalclaims: 
            
                
            newnumberdice=rerollifzero(numberofdice-len(legalclaim))
            newscore=tempscore+scoreclaim(legalclaim)
            bankclaimprob=bankingwinprob(playerscore,opponentscore,newnumberdice,newscore,True)
            bankingprobs.append(bankclaimprob)

        winprob=max(bankingprobs)

    else: #winprob is 1-opponent's winprob with no update to score
        winprob=1-bankingwinprob(opponentscore,playerscore,6,0,True)

    return winprob


#winprobdatabase=numpy.full((20,20,6,20),0.5); #initialise the 
#setwins(winprobdatabase)



#This needs to be in the same file, as otherwise, bankingwinprob and scoringwinprob
#do not have access to the lookup database, for some reason


#winprobdatabase=numpy.load("bankingdatabase2player.npy")

def sweep():
    delta=0
    for playerscore in range(950,-50,-50):
        for opponentscore in range(950,-50,-50):
            for dice in range(6,0,-1):
                for tempscore in range(950,-50,-50):
                    if playerscore+tempscore<1000:
                        oldwinprob=winprobdatabase[int(playerscore/50),int(opponentscore/50),dice-1,int(tempscore/50)]
                        winprob=bankingwinprob(playerscore,opponentscore,dice,tempscore)
                        winprobdatabase[int(playerscore/50),int(opponentscore/50),dice-1,int(tempscore/50)]=winprob
                        delta=max(delta,abs(oldwinprob-winprob))
    return delta


def valueiterate(tol):

    
    delta=1
    while delta>tol:
        start=time.time()
        delta=sweep()
        end=time.time()
        print("Completed sweep in ",end-start,"! , delta = ",delta,", tol = ",tol)
        numpy.save("bankingdatabase2player",winprobdatabase)

        
#winprobdatabase=numpy.full((20,20,6,20),0.5); #initialise the 
winprobdatabase=numpy.load("bankingdatabase2player.npy")
#setwins(winprobdatabase)
lookuptable=getrolllookup()#returns all unique dice rolls with 1,2,3,4,5,6 dice
legalclaimslookup=getlegalclaimlookup()
valueiterate(1e-4)
print(winprobdatabase[0,0,5,0])
print(winprobdatabase[10,0,3,2])
##start=time.time()
##for i in range(10):
##    for j in range(10):
##        for k in range(6):
##            a=bankingwinprob(i*50,j*50,k+1,500)
##end=time.time()
##print(end-start)
