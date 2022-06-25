
import requests
url = 'https://api.jsonbin.io/v3/b/62b6a6d6402a5b380238a721/'
headers = {
  'X-Master-Key': '$2b$10$N.z2Kwz/hDVThtJ6GNi.suZ9NKOF9n1Oji.ROGs.z8wSfZi2mlrUa',
  'Content-Type': 'application/json'
}

data = {""}
req = requests.get(url, json=None, headers=headers)
print(req.text)