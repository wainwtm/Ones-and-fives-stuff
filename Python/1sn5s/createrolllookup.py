#Function which takes as input a number of dice and returns list of all possible scoring rolls
from collections import Counter
import json
def numtobase6list(n,dice):
    l=[]
    for i in range(1,dice+1):
        factor=dice-i
        quotient=n//(6**factor)
        n=n-quotient*6**factor
        l.append(quotient+1)
    return l

def outputlist(numberofdice):
    seenlist=[]
    alllist=[]
    seeninfo=[]
    for i in range(6**numberofdice):
            dice=numtobase6list(i,numberofdice)
            originallength=len(dice)
            # converts [1,2,3,4,4,6] to [1,x,x,x,x,x]
            #if not straight:
            #   takes all numbers !=1,5 of frequency < 3 and changes to x

            counter=Counter(dice) #convert to dice frequencies
            frequencies=[counter[x] for x in [1,2,3,4,5,6]]
            if frequencies!=[1,1,1,1,1,1]:
                for i in [2,3,4,6]:
                    if frequencies[i-1]<3:
                        frequencies[i-1]=0
            dice=[]
            for i in range(6):
                if frequencies[i]>0:
                    for j in range(frequencies[i]):
                        dice.append(i+1)

                    
            newlength=len(dice)
            lengthdiff=originallength-newlength
            if lengthdiff>0:
                for i in range(lengthdiff):
                    dice.append("x")
            alllist.append(dice)            
    for item in alllist:
        if not(item in seenlist):
            seenlist.append(item)
            
    for item in seenlist:
        seeninfo.append([item,alllist.count(item)])        
    return seeninfo
        

rolllookup=[]
for i in range(1,7):
    rolllookup.append(outputlist(i))

            
with open("rolllookup.json", 'w') as f:
    # indent=2 is not needed but makes the file human-readable 
    # if the data is nested
    json.dump(rolllookup, f, indent=2) 

          
            
