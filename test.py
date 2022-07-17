import json

f = open('demo.json')
raw = json.load(f)
maindata = raw['data']
k = list(maindata.keys())
print(maindata['user1']['passw'])
if 'user1' in k and 1234 == maindata['user1']['passw']:    
  print('true')