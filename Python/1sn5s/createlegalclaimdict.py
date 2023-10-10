import json
from itertools import product
from collections import Counter
from analyticalutilities import *

rolllookup=getrolllookup()

legalclaimdict={}
for i in range(6):
    for roll in rolllookup[i]:
        legalclaimdict[str(roll[0])]=findlegalclaims(roll[0])
dictkey=str([1,5,"x","x","x","x"])


with open("legalclaims.txt", "w") as fp:
    json.dump(legalclaimdict, fp)  # encode dict into JSO

reasonableclaimdict = {}

for i in range(6):
    for roll in rolllookup[i]:
        legalclaims=findlegalclaims(roll[0])
        reasonableclaims=[]
        scores=[0,0,0,0,0,0]
        for claim in legalclaims:
            claimsize = len(claim)
            claimscore = scoreclaim(claim)
            if claimscore > scores[claimsize-1]:
                scores[claimsize-1] = claimscore
        for i in range(6):
            if scores[i]>0:
                reasonableclaims.append([i+1,scores[i]])
        reasonableclaimdict[str(roll[0])]=reasonableclaims        
            
            
dictkey=str([1,1,5,5,5,5])
print(reasonableclaimdict[dictkey])
with open("reasonableclaims.txt", "w") as fp:
    json.dump(reasonableclaimdict, fp)  # encode dict into JSO
