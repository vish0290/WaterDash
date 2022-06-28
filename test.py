import requests,json
url = 'https://api.jsonbin.io/v3/b/62babd40192a674d291dfc83/'
headers = {
  'X-Master-Key': '$2b$10$5xrR.z3jZ3mxMw1V4R8vWe.1A5P2iJ4mpP8AHtqtKE3ozSJ41NFOC'
}


def update_date(uid,fi,val):
    #read data
    req = requests.get(url,headers=headers)
    raw_data = json.loads(req.content.decode("UTF-8"))
    data = raw_data['record']
    maindata = data[uid]
    if fi in maindata.keys(): 
        maindata[fi] = val
        data[uid] = maindata       
        res = requests.put(url,json=data, headers= headers)
        print(res)
    else:
        print("Field is not present") 


update_date('user1', 'data', 25)

