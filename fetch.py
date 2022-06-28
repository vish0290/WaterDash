
import requests, json
url = 'https://api.jsonbin.io/v3/b/62b6a6d6402a5b380238a721/latest'
headers = {
  'X-Master-Key': '$2b$10$N.z2Kwz/hDVThtJ6GNi.suZ9NKOF9n1Oji.ROGs.z8wSfZi2mlrUa',
  'Content-Type': 'application/json'
}



#read data
req = requests.get(url,headers=headers)
raw_data = json.loads(req.content.decode("UTF-8"))
data = raw_data['record']
print(data)

#update data
# data = {"user":{"data":25}}
# req = requests.put(url, json=data, headers=headers)
