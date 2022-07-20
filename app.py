from flask import Flask, jsonify, request, render_template, redirect
import json,os
import requests
import pyrebase
from datetime import date
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
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


@app.route('/', methods = ['GET', 'POST'])
def home():
    if session:
        raw = json.loads(json.dumps(db.child('data').get().val()))
        global cid 
        a = date.today()
        current_month = '{:02d}'.format(a.month)+'-'+str(a.year)
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
        
        user = cid
        data = raw[user]['date']
        date_keys =data.keys()
        flowrate = raw[user]['flowrate']
        volumes = [data[i]['volume'] for i in date_keys]
        temp_dict = []
        for i in date_keys:
            d = {"date":i, "volume in liters":data[i]['volume']  }
            temp_dict.append(d)
        df = pd.DataFrame(temp_dict)
        fig = px.line(df, x="date", y="volume in liters")
        fig.write_image("static/img/water_vol.png")
        
        data = raw[user]['bill']
        date_keys =data.keys()
        volumes = [data[i]['bill_amount'] for i in date_keys]
        temp_dict = []
        for i in date_keys:
            d = {"date":i, "bill amount":data[i]['bill_amount']  }
            temp_dict.append(d)
        df = pd.DataFrame(temp_dict)
        fig = px.line(df, x="date", y="bill amount")
        fig.write_image("static/img/bill.png")
        
        fig = go.Figure(go.Indicator(
        mode = "gauge+number",
        value = raw[user]['flowrate'],
        gauge={'axis':{"range":[None,8]},
            'bar':{'color':'red'}
            },
        domain = {'x': [0, 1], 'y': [0, 1]},
        ))
        fig.write_image("static/img/flowrate.png")
        
        data = raw[user]['date']
        date_keys =data.keys()
        temp_dict = []
        for i in date_keys:
            d = {"date":i, "water level":data[i]['water_lvl']  }
            temp_dict.append(d)
        print(temp_dict)

        df = pd.DataFrame(temp_dict)
        fig = px.bar(df, x="date", y="water level")
        fig.write_image('static/img/water_lvl.png')
        return render_template('index.html', data = data_dic, flow=flowrate)
    return redirect('/login')

@app.route('/logout',methods=['POST','GET'])
def logout():
    global session
    session=False
    return redirect('/login')

@app.route('/logs',methods=['GET','POST'])
def logs():
    if session:
        global cid 
        raw = json.loads(json.dumps(db.child('data').get().val()))
        a = date.today()
        current_month = '{:02d}'.format(a.month)+'-'+str(a.year)
        usne_enter_kiya = cid
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
    

# @app.route('/update/<string:val>', methods=['POST'])
# def process_data(val):
    
#     raw = json.loads(json.dumps(db.child('data').get().val()))
#     a = date.today()
#     current_date = str(a.day)+'-'+'{:02d}'.format(a.month)+'-'+str(a.year)
#     # content_type = request.headers.get('Content-Type')
#     # if (content_type == 'application/json'):
#     #     json_data = request.json
#     #     user = json_data['user']
#     #     flow = json_data['flowrate']
#     #     lvl = json_data['water_lvl']
#     #     vol = json_data['volume']
#     #     dates_data = raw[user]['date']
#     itab = val.split(':')
#     dates_data.update({current_date:{'volume':itab[1],'water_lvl':itab[2]}})
#     data = {'flowrate':itab[3],'date':dates_data}
#     return db.child('data').child(itab[0]).update(data)
         
#     # else:
#     #     return 'Content-Type not supported!'
#     # return print('pass')


@app.route('/update/<string:val>')
def passdata(val):
    raw = json.loads(json.dumps(db.child('data').get().val()))
    a = date.today()
    itab = val.split(':')
    current_date = str(a.day)+'-'+'{:02d}'.format(a.month)+'-'+str(a.year)
    val = val.split(':')
    print(val)
    dates_data=raw[itab[0]]['date']
    if itab[4] == '1':
        flag = True 
    dates_data.update({current_date:{'volume':int(float(itab[1]))}})
    data = {'flowrate':float((itab[3])),'date':dates_data,'limit':flag}
    db.child('data').child(itab[0]).update(data)
    print(val)
    return str(val)

@app.route('/payment')
def payment():
    raw = json.loads(json.dumps(db.child('data').get().val()))
    global cid
    a = date.today()
    cur = '{:02d}'.format(a.month)+'-'+str(a.year)
    dic = {
        'uname':cid,
        'name':raw[cid]['name'],
        'bill_no':raw[cid]["bill"][cur]['bill_no'],
        'bill_date':raw[cid]["bill"][cur]['bill_date'],
        'bill_amount':raw[cid]["bill"][cur]['bill_amount'],
        'phone':raw[cid]['phno'],
        'email':raw[cid]['email'],
        'address':raw[cid]['address']
    }
    return render_template('payments.html', data=dic)

@app.route('/login',methods=['GET','POST'])
def login():
    raw = json.loads(json.dumps(db.child('data').get().val()))
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
    app.run(host='0.0.0.0', port=50000, debug=True)
    