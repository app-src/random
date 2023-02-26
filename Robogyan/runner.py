import json
import firebase as fb
  
# Opening JSON file
f = open('Robogyan/data.json')
  
# returns JSON object as 
# a dictionary
data = json.load(f)
  
# Iterating through the json
# list
for i in data['items']:
    fb.don(i['name'])
  
# Closing file
f.close()

