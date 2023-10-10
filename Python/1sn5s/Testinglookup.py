import json
def getrolllookup():
    with open("rolllookup.json", 'r') as f:
        return json.load(f)

