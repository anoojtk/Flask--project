from flask import Flask,render_template,request
import pickle
import numpy as np
import pandas as pd
app=Flask(__name__)
model=pickle.load(open('model.pkl','rb'))
@app.route('/')
def climate():
    return render_template('used bikes.html')
@app.route('/predict',methods=['post'])
def predict():
    owner=float(request.values['owner'])
    print("owner",owner)
    age=int(request.values['age'])
    print("age",age)
    power=float(request.values['power'])
    print("power",power)
    brand=float(request.values['brand'])
    print("brand",brand)



    data=[[owner,age,power,brand]]
    df=pd.DataFrame(data,columns=['owner','age','power','brand'])
    a=model.predict(df)
    print('bike price is :',a)
    return render_template('used bikes.html',prediction=a)
if __name__=='__main__':
    app.run(port=8000)