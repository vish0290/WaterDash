from flask import Flask, jsonify, request, render_template, redirect
import json,os
import requests
import pyrebase
from test2 import update_field
# creating a Flask app
app = Flask(__name__)
session = False

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

current_month = "04-2022"
usne_enter_kiya="user2"
# Name
# Address
# Bill amount
# Status
# Date Name Address Bill Status 

# data_dic = {
#     'name': raw[usne_enter_kiya]["name"],
#     "address" : raw[usne_enter_kiya]["address"],
#     "bill_amount" : raw[usne_enter_kiya]['bill'][current_month]["bill_amount"],
#     "status" : raw[usne_enter_kiya]['bill'][current_month]["status"]
# }

# headings = ['Date','Name','Address','Bill Amount','Status']

# data_got = []

# dates = raw[usne_enter_kiya]['bill'].keys()

# for i in dates:
#       temp = []
#       temp.append(i)
#       temp.append(raw[usne_enter_kiya]["name"])
#       temp.append(raw[usne_enter_kiya]["address"])
#       temp.append(raw[usne_enter_kiya]['bill'][i]["bill_amount"])
#       temp.append(raw[usne_enter_kiya]['bill'][i]["status"])
#       data_got.append(tuple(temp))


from datetime import date
a = date.today()
print('{:02d}'.format(a.month)+'-'+str(a.year))