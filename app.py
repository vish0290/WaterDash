from flask import Flask, jsonify, request, render_template, redirect
import json,os
import requests
import pyrebase
from test2 import update_field
# creating a Flask app
app = Flask(__name__)
session = False
cid = ""

config={  
"apiKey": "AIzaSyCc0veJ4Kez3iLS8U-qjxhOMFwnzA7WZ7U",
  "authDomain": "fir-46336.firebaseapp.com",
  "databaseURL": "https://fir-46336-default-rtdb.asia-southeast1.firebasedatabase.app",
  "projectId": "fir-46336",
  "storageBucket": "fir-46336.appspot.com",
  "messagingSenderId": "1021317922890",
  "appId": "1:1021317922890:web:71550b203e9eb04f8de6b3",
  "measurementId": "G-RGCMC81BWC"}

firebase=pyrebase.initialize_app(config)
db = firebase.database()
raw = json.loads(json.dumps(db.child('data').get().val()))


@app.route('/', methods = ['GET', 'POST'])
def home():
    if session:
        global cid
        current_month = "04-2022"
        usne_enter_kiya = cid
        # Name
        # Address
        # Bill amount
        # Status
        
        data_dic = {
            'name': raw[usne_enter_kiya]["name"],
            "address" : raw[usne_enter_kiya]["address"],
            "bill_amount" : raw[usne_enter_kiya]['bill'][current_month]["bill_amount"],
            "status" : raw[usne_enter_kiya]['bill'][current_month]["status"]
        }

        print(data_dic)
        return render_template('index.html', data = data_dic)
    return redirect('/login')

@app.route('/logs',methods=['GET','POST'])
def logs():
    if session:
        current_month = "04-2022"
        usne_enter_kiya="user1"
        # Name
        # Address
        # Bill amount
        # Status
        # Date Name Address Bill Status 
        
        data_dic = {
            'name': raw[usne_enter_kiya]["name"],
            "address" : raw[usne_enter_kiya]["address"],
            "bill_amount" : raw[usne_enter_kiya]['bill'][current_month]["bill_amount"],
            "status" : raw[usne_enter_kiya]['bill'][current_month]["status"]
        }
        
        headings = ['Date','Name','Address','Bill Amount','Status']
       
        data_got = []

        dates = raw[usne_enter_kiya]['bill'].keys()

        for i in dates:
            temp = []
            temp.append(i)
            temp.append(raw[usne_enter_kiya]["name"])
            temp.append(raw[usne_enter_kiya]["address"])
            temp.append(raw[usne_enter_kiya]['bill'][i]["bill_amount"])
            temp.append(raw[usne_enter_kiya]['bill'][i]["status"])
            data_got.append(tuple(temp))

        return render_template('logs.html', data = data_dic, heading=headings, rows=data_got)
    

@app.route('/post_json', methods=['POST'])
def process_json():
    content_type = request.headers.get('Content-Type')
    if (content_type == 'application/json'):
        json_data = request.json
        return db.update(json_data)
    else:
        return 'Content-Type not supported!'


@app.route('/payment')
def payment():
    return render_template('payments.html')

@app.route('/login',methods=['GET','POST'])
def login():
    if request.method == "POST":
        uid = request.form.get('uname')
        passw = request.form.get('passw')
        if uid in list(raw.keys()):
            if passw == raw[uid]['passw']:
                global session, cid
                session = True
                cid =  uid
                return redirect('/')
            else:
                print('Wrong password')
        else:
            print('No user')
    else:
        print('post not working')
    return render_template('login.html')
        
# @app.route('/update/<string:fid>:<string:val>', methods=['GET'])
# def update_field(fid,val):  
#     firebase=pyrebase.initialize_app(config)
#     data = {fid:val}
#     db = firebase.database()
#     return  db.update(data) 

    
if __name__ == '__main__':
  
    # app.run(debug = False, host='0.0.0.0')
    # app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))
    # app.run()
    # port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0')
    