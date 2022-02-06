
from flask import Flask, request
import pandas as pd
import numpy as np
import pickle
import flasgger
from flasgger import Swagger
from flask import Flask,request,jsonify
from sklearn.model_selection import train_test_split



app = Flask(__name__)
Swagger(app)

# From which point yuu want to sart this application
#app=Flask(__name__)
pickle_in = open(r'modelwave.pkl', 'rb')
modelwave = pickle.load(pickle_in)

pickle_in = open(r'modelripple.pkl', 'rb')
modelripple= pickle.load(pickle_in)

@app.route('/')
def welcome():
    return "Welcome All"



@app.route('/predictwave',methods=['POST'])
def predictwave():
    content = request.json
    df = pd.DataFrame(content)
        
    dictToReturn = modelwave.predict(df).tolist()
    return jsonify(dictToReturn)


@app.route('/predictripple',methods=['POST'])
def predictripple():
    content = request.json
    df = pd.DataFrame(content)
        
    dictToReturn = modelripple.predict(df).tolist()
    return jsonify(dictToReturn)

if __name__ == '__main__':
    #app.run(debug=True)
    app.run(host='0.0.0.0',port=6000)
    