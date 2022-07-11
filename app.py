from flask import Flask, jsonify, request
import json,os
import requests
import pyrebase
from test2 import update_field
# creating a Flask app
app = Flask(__name__)

url = 'https://api.jsonbin.io/v3/b/62babd40192a674d291dfc83/'
headers = {
  'X-Master-Key': '$2b$10$5xrR.z3jZ3mxMw1V4R8vWe.1A5P2iJ4mpP8AHtqtKE3ozSJ41NFOC',
  'Content-Type': 'application/json'
}

config={  
"apiKey": "AIzaSyCc0veJ4Kez3iLS8U-qjxhOMFwnzA7WZ7U",
  "authDomain": "fir-46336.firebaseapp.com",
  "databaseURL": "https://fir-46336-default-rtdb.asia-southeast1.firebasedatabase.app",
  "projectId": "fir-46336",
  "storageBucket": "fir-46336.appspot.com",
  "messagingSenderId": "1021317922890",
  "appId": "1:1021317922890:web:71550b203e9eb04f8de6b3",
  "measurementId": "G-RGCMC81BWC"}


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



@app.route('/update/<string:fid>:<string:val>', methods=['GET'])
def update_field(fid,val):  
    firebase=pyrebase.initialize_app(config)
    data = {fid:val}
    db = firebase.database()
    return  db.update(data) 

    
if __name__ == '__main__':
  
    # app.run(debug = False, host='0.0.0.0')
    # app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))
    # app.run()
    # port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0')
    