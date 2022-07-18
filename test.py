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

# current_month = "04-2022"
# usne_enter_kiya="user2"
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


# from datetime import date
# a = date.today()
# print('{:02d}'.format(a.month)+'-'+str(a.year))

import plotly.express as px
import pandas as pd

raw = json.loads(json.dumps(db.child('data').get().val()))
user = 'user1'
# data = raw[user]['date']
# date_keys =data.keys()
# volumes = [data[i]['volume'] for i in date_keys]
# temp_dict = []

# for i in date_keys:
#       d = {"date":i, "volume in liters":data[i]['volume']  }
#       temp_dict.append(d)
# print(temp_dict)

# df = pd.DataFrame(temp_dict)
# print(df)
# # df = px.data.gapminder().query("country=='Canada'")
# fig = px.line(df, x="date", y="volume in liters", title='Water Consumption')
# fig.write_image("static/img/water_vol.png")



# fig = go.Figure(go.Indicator(
#     mode = "gauge+number",
#     value = raw[user]['flowrate'],
#     gauge={'axis':{"range":[None,8]},
#            'bar':{'color':'red'}
#            },
#     domain = {'x': [0, 1], 'y': [0, 1]},
#     title = {'text': "Speed"}))

# import plotly.express as px
# data = raw[user]['date']
# date_keys =data.keys()
# temp_dict = []
# for i in date_keys:
#       d = {"date":i, "water level":data[i]['water_lvl']  }
#       temp_dict.append(d)
# print(temp_dict)

# df = pd.DataFrame(temp_dict)
# fig = px.bar(df, x="date", y="water level",color_discrete_map={
#         'some_group': 'red',
#         'some_other_group': 'green'
#     })
# # fig = px.histogram(df, x="date")
# fig.show()










# import matplotlib.pyplot as plt
# import pandas as pd
  
# # Defining index for the dataframe
# idx = ['1', '2', '3', '4']
  
# # Defining columns for the dataframe
# cols = list('ABCD')
  
# # Entering values in the index and columns  
# # and converting them into a panda dataframe
# df = pd.DataFrame([[10, 20, 30, 40], [50, 30, 8, 15],
#                    [25, 14, 41, 8], [7, 14, 21, 28]],
#                    columns = cols, index = idx)
  
# # Displaying dataframe as an heatmap
# # with diverging colourmap as RdYlBu
# plt.imshow(df, cmap ="RdYlBu")
  
# # Displaying a color bar to understand
# # which color represents which range of data
# plt.colorbar()
  
# # Assigning labels of x-axis 
# # according to dataframe
# plt.xticks(range(len(df)), df.columns)
  
# # Assigning labels of y-axis 
# # according to dataframe
# plt.yticks(range(len(df)), df.index)
  
# # Displaying the figure
# plt.show()



import requests

url = 'http://127.0.0.1:50000/post_json'
jsondata = {'user':'user1','flowrate':4.8,'volume':80,'water_lvl':45}
resp = requests.post(url,json=jsondata) 
print(resp)