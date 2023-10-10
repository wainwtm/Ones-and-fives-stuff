import json
from itertools import product
from collections import Counter

def getrolllookup():
    with open("rolllookup.json", 'r') as f:
        return json.load(f)
def getlegalclaimlookup():
    with open("legalclaims.txt", "r") as f:
        return json.load(f)
def getreasonableclaimlookup():
    with open("reasonableclaims.txt", "r") as f:
        return json.load(f)


def rolllivesprob(n):
    if n==1:
        return 1/3
    elif n==2:
        return 5/9
    elif n==3:
        return 13/18
    elif n==4:
        return 91/108
    elif n==5:
        return 299/324
    elif n==6:
        return 157/162
    else:
        pass
def listlegalclaims(dice):
    key=str(dice)
    return legalclaims[key]

def findlegalclaims(dice):
    #takes a set of dice, and returns a list of legal claims
    #and their associated score
    # dice are inputted in form [1,1,5,x,x,x]
    # [5,5,5,1,x,x], [1,2,3,4,5,6], etc.
    legalclaims=[]
    counter=Counter(dice) #convert to dice frequencies
    frequencies=[counter[x] for x in [1,2,3,4,5,6]]

    
    if frequencies==[1,1,1,1,1,1]:
        legalclaims=[[1,2,3,4,5,6],[1],[5]]
    else:
        legalonesclaims=[[]]
        legalfivesclaims=[[]]
        legalsetclaims=[[]]
        if frequencies[0]>0: #ones
            for i in range(frequencies[0]):
                legalonesclaims.append([1]*(i+1))


        if frequencies[4]>0: #fives
            for i in range(frequencies[4]):
                legalfivesclaims.append([5]*(i+1))

        for i in [1,2,3,5]: #look for sets
            if frequencies[i]>=3:
                for j in range(3,frequencies[i]+1):
                    legalsetclaims.append([i+1]*j)


                #hacky fix for cases of two disjoint sets
        if len(legalsetclaims)>2 and legalsetclaims[1][0]!=legalsetclaims[2][0]:
            legalsetclaims=[[],legalsetclaims[1],legalsetclaims[2],legalsetclaims[1]+legalsetclaims[2]]
                    

        for legaloneclaim in legalonesclaims: #take product of claim types
            for legalfiveclaim in legalfivesclaims:
                for legalsetclaim in legalsetclaims:
                    legalclaim=legaloneclaim+legalfiveclaim+legalsetclaim
                    legalclaims.append(legalclaim)
        legalclaims.remove([])
        
        
    return legalclaims    

def scoreclaim(claim):
    counter=Counter(claim)#convert to frequencies
    frequencies=[counter[x] for x in [1,2,3,4,5,6]]
    score=0
    if frequencies==[1,1,1,1,1,1]:#123456
        score+=2000
    else:
        for i in range(1,7):
            if frequencies[i-1]>=3: #if there is a set of >=3
                if i==1:
                    basescore=1000
                else:
                    basescore=100*(i)
                score+=basescore*2**(frequencies[i-1]-3)

                

            else:
                if i==1:
                    score+=100*frequencies[i-1]
                            
                if i==5:
                    score+=50*frequencies[i-1]
    return score

def scorelist(claims):
    scoredlist=[]
    for item in claims:
        score=scoreclaim(item)
        if score>0:
            scoredlist.append([item,score])
    return scoredlist

def findmax(claims):
    maximum=0
    for item in claims:
        if item[1]>maximum:
            maximum=item[1]
    return maximum
    

def rerollifzero(n):
    if n==0:
        return 6
    else:
        return n

def listlegalclaimsbasic(dice):

    #To match the ruleset of the paper
    
    #takes a set of dice, and returns a list of legal claims
    #and their associated score
    # dice are inputted in form [1,1,5,x,x,x]
    # [5,5,5,1,x,x], [1,2,3,4,5,6], etc.
    legalclaims=[]
    counter=Counter(dice) #convert to dice frequencies
    frequencies=[counter[x] for x in [1,2,3,4,5,6]]
    legalonesclaims=[[]]
    legalfivesclaims=[[]]
    legalsetclaims=[[]]
    if frequencies[0]>0: #ones
        for i in range(frequencies[0]):
            legalonesclaims.append([1]*(i+1))


    if frequencies[4]>0: #fives
        for i in range(frequencies[4]):
            legalfivesclaims.append([5]*(i+1))

    for i in [1,2,3,5]: #look for sets
        if frequencies[i]==3:
            legalsetclaims.append([i+1]*3)


            #hacky fix for cases of two disjoint sets
            if len(legalsetclaims)>2 and legalsetclaims[1][0]!=legalsetclaims[2][0]:
                legalsetclaims=[[],legalsetclaims[1],legalsetclaims[2],legalsetclaims[1]+legalsetclaims[2]]
                

    for legaloneclaim in legalonesclaims: #take product of claim types
        for legalfiveclaim in legalfivesclaims:
            for legalsetclaim in legalsetclaims:
                legalclaim=legaloneclaim+legalfiveclaim+legalsetclaim
                legalclaims.append(legalclaim)
    legalclaims.remove([])
        
        
    return legalclaims 


    
