#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pickle
from flask import Flask,request
import numpy as np
import pandas as pd
with open('random_forest.pkl','rb') as model_file:
    model = pickle.load(model_file)

app = Flask(__name__)

@app.route('/predict',methods=['POST'])
def predict_iris():
    """
    Example endpoint returning a prediction of iris
    
    """
    s_length = request.form['s_length']
    s_width = request.form['s_width']
    p_length = request.form['p_length']
    p_width = request.form['p_width']
    
    prediction = model.predict(np.array([[s_length,s_width,p_length,p_width]]))
    if prediction == [0]:
        return 'Iris Setosa'
    if prediction == [1]:
        return 'Iris Versicolor'
    else:
        return 'Iris Virginica'
    

if __name__=='__main__':
    app.run(host='0.0.0.0', port=5000)

