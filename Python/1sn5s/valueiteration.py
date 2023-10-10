from analyticalutilities import *
from twoplayergame import *



#bankingwinprob(playerscore,opponentscore,numberofdice,tempscore)
#returns the probability of a game win from banking decision state
#with when holding 'numberofdice' dice, and
#where banking would result in tempscore,
#bringing your total score to playerscore+tempscore (and beginning your opponenent's turn)

#The first time bankingwinprob is run, it calculates probability of a win
#By taking the maximum of 


winprobdatabase=numpy.full((20,20,6,20),0.5); #initialise the 
setwins(winprobdatabase)
lookuptable=getrolllookup()



#setwins(bankingdatabase)

#winprobdatabase=numpy.load("bankingdatabase2player.npy")
progress=0
maxprogress=20*20*6*20
differences=[]

for playerscore in range(19,-1,-1):
    totaldiff=0
    batchlength=0
    for opponentscore in range(19,-1,-1):
        for dice in range(6,0,-1):
            for tempscore in range(19,-1,-1):
                if playerscore+tempscore<20:
                    #totaldiff+=bankingwinprob(playerscore*50,opponentscore*50,dice,tempscore*50,False)
                    #progress+=1
                    #batchlength+=1
                    differences.append(bankingwinprob(playerscore*50,opponentscore*50,dice,tempscore*50))
    #numpy.save('bankingdatabase2player', bankingdatabase)
    #print("did a batch and changed a total of",totaldiff)
    #print(progress,"/",maxprogress)
    #print("In this batch, average change is ",totaldiff/batchlength) 
numpy.save('bankingdatabase2player', winprobdatabase)
print("biggest change: ",max(differences))
