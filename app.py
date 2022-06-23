from flask import Flask, jsonify, request
import json,os
# creating a Flask app
app = Flask(__name__)


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
    file = 'data.json'
    f = open(file ,'r')
    rawdata = json.load(f)
    f.seek(0)
    f.close()
    maindata = rawdata[uid]
    if fi in maindata.keys(): 
        maindata[fi] = val
        rawdata[uid] = maindata
        with open(file,'w') as w:
            json.dump(rawdata,w,indent=4)
            return jsonify(rawdata)
    else:
        print("Field is not present") 
    
if __name__ == '__main__':
  
    # app.run(debug = False, host='0.0.0.0')
    # app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))
    # app.run()
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
    