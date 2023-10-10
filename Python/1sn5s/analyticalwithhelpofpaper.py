from analyticalutilities import *
from onesandfives import Turn

import json
import numpy

bankingdatabase=numpy.zeros((7,2001))
#hardcode inaccessible values
inaccessiblevalues=[[5,0],[4,0],[3,0],[2,0],[1,0],[4,1],[3,1],[2,1],[1,1],[3,2],[2,2],[1,2],[2,3],[1,3],[1,4],[6,1],[6,2],[6,3],[6,4],[6,5],[5,3],[5,4],[5,5],[5,6],[4,5],[4,6],[4,7],[3,7]]
for coords in inaccessiblevalues:
    bankingdatabase[coords[0],coords[1]]=10000000

lookuptable=getrolllookup()

def bankinggain(numberofdice,score):
    
    if bankingdatabase[numberofdice,int(score/50)]!=0: #if our expectation has been done already
        scoreexpectation=bankingdatabase[numberofdice,int(score/50)]
        #print("I looked something up")
        #print("action for ",numberofdice,score," has already been calculated.")

    elif score<=0:
        sumofbankexpectations=0
        for roll in lookuptable[numberofdice-1]:
            rollfrequency=roll[1]
            rolldice=roll[0]
            
            #to show progress
                
            sumofbankexpectations+=rollfrequency*scoringgain(numberofdice,score,rolldice)

        scoreexpectation=sumofbankexpectations/(6**numberofdice)

    #search vast database of previously found bankinggains :)
       
    elif score>20000:
        #you would always bank here
        scoreexpectation=score

    
    

 
    
    
        
        
    
    
    else:
        sumofbankexpectations=0
        for roll in lookuptable[numberofdice-1]:
            rollfrequency=roll[1]
            rolldice=roll[0]
            
            sumofbankexpectations+=rollfrequency*scoringgain(numberofdice,score,rolldice)

        bankexpectation=sumofbankexpectations/(6**numberofdice)

        scoreexpectation=max(bankexpectation,score)

    bankingdatabase[numberofdice,int(score/50)]=scoreexpectation

    return scoreexpectation
        

def scoringgain(numberofdice,score,roll):
    bankinggains=[]
    legalclaims=listlegalclaims(roll)
    
    #print("finding scoring gain on ",numberofdice,score,roll)
    
    if legalclaims!=[]:
        for legalclaim in legalclaims:
            newnumberdice=rerollifzero(numberofdice-len(legalclaim))
            newscore=score+scoreclaim(legalclaim)
            bankclaimexpectation=bankinggain(newnumberdice,newscore)
            bankinggains.append(bankclaimexpectation)
        scoringgain=max(bankinggains)
        #print("best action on ",numberofdice,score,roll," is", maximum)
    else:
        scoringgain=0
    return scoringgain

def listlegalclaims(dice):
    key=str(dice)
    return legalclaims[key]



legalclaims=getlegalclaimlookup()
print(bankinggain(6,0))

for i in range(7):
    for j in range(2001):
        if bankingdatabase[i,j]!=0:
            bankingdatabase[i,j]=bankingdatabase[i,j]-50*j

for n in range(1,7):
    j=1
    looping=True
    while looping:
        if bankingdatabase[n,j]==0:
            print("Optimally, you stop ", n,"- rolling after ",(j-2)*50) 
            looping=False
        j+=1


        
numpy.savetxt('bankingdatabase.csv', bankingdatabase, delimiter=',')
    
    
