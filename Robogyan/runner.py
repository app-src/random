import json
import firebase as fb
  
# Opening JSON file
o = open('Robogyan/old.json')
n = open('Robogyan/new.json')
  
# returns JSON object as 
# a dictionary
old = json.load(o)
new = json.load(n)

# Iterating through the json
# list
cou=0
for i in new['items']:
    if i not in(old['items']):
        cou+=1
        fb.don(i['name'])
        print(cou)
  
# Closing file
o.close()
n.close()

