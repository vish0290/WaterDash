from flask import Flask, jsonify, request, render_template
import json,os
import requests
import pyrebase
from test2 import update_field
# creating a Flask app
app = Flask(__name__)


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
        return render_template('index.html')

@app.route('/post_json', methods=['POST'])
def process_json():
    content_type = request.headers.get('Content-Type')
    if (content_type == 'application/json'):
        json_data = request.json
        return db.update(json_data)
    else:
        return 'Content-Type not supported!'


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
    