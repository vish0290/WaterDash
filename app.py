from flask import Flask, jsonify, request
import json,os
# creating a Flask app
app = Flask(__name__)

url = 'https://api.jsonbin.io/v3/b/62babd40192a674d291dfc83/'
headers = {
  'X-Master-Key': '$2b$10$5xrR.z3jZ3mxMw1V4R8vWe.1A5P2iJ4mpP8AHtqtKE3ozSJ41NFOC',
  'Content-Type': 'application/json'
}



@app.route('/', methods = ['GET', 'POST'])
def home():
        return "<h1>Hello there </h1>"




#  Authentication
@app.route('/login/<string:uid>:<string:passw>', methods = ['GET','POST']) 
def login(uid,passw):
    f = open('data.json')
    maindata = json.load(f)
    f.close()
    if uid in maindata.keys():
        data = maindata[uid]
        if data['pass'] == passw:
            return "Success"
            user_id = uid
            log = True
        else:
            return "Wrong Pass"
    else:
        return "User does not exist" 

@app.route('/update/<string:uid>:<string:fi>:<string:val>', methods = ['GET','POST'])
def update_date(uid,fi,val):
    req = requests.get(url,headers=headers)
    raw_data = json.loads(req.content.decode("UTF-8"))
    data = raw_data['record']
    maindata = data[uid]
    if fi in maindata.keys(): 
        maindata[fi] = val
        data[uid] = maindata       
        res = requests.put(url,json=data, headers= headers)
    else:
        return "<h1>Field is not present</h1>"

    
if __name__ == '__main__':
  
    # app.run(debug = False, host='0.0.0.0')
    # app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))
    # app.run()
    # port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0')
    