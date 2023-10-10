import json
def getrolllookup():
    with open("rolllookup.json", 'r') as f:
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
