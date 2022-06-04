from datetime import datetime
from flask_cors import CORS
from flask import Flask,render_template,request
import requests
import time
import json

app=Flask(__name__)
CORS(app)

get_url='https://0c0elmusa2.execute-api.us-east-1.amazonaws.com/Prod/get/data'
post_url='https://0c0elmusa2.execute-api.us-east-1.amazonaws.com/Prod/senddata/sqs'

@app.route('/')
def helloPage():
    return render_template('index.html')

@app.route('/postMessage',methods=['GET','POST'])
def collectMessage():
    msg=request.form['msg']
    print(datetime.now())
    print(msg)
    k={'name':str(datetime.now()),'message':msg}
    result=requests.post(post_url,json=k)
    print(result,result.text)
    return ('posted successfully')

@app.route('/getMessages',methods=['GET','POST'])
def readMessage():
    k=requests.get(get_url)
    print(k.text)
    return(json.loads(k.text))
    
if __name__=="__main__":
    app.run(debug=True)