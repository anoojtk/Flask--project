from flask import Flask,render_template,request
import pickle
import numpy as np
import pandas as pd
app=Flask(__name__)
model=pickle.load(open('model.pkl','rb'))
@app.route('/')
def climate():
    return render_template('weather.html')
@app.route('/predict',methods=['post'])
def predict():
    tem=float(request.values['climate'])
    print(tem)
    wind=float(request.values['climate'])
    print(wind)

    data = [[tem, wind]]
    df = pd.DataFrame(data, columns=['temp_max', 'wind'])
    x=model.predict(df)
    
    if x<=0:
        print('weather is Drizzer')
        x='weather is Drizzer'
    elif x>0 or x<=2:
        print('weather is Rain')
        x='weather is Rain'
    elif x>2 or x<=3:
        print('weather is Sun')
        x='weather is Sun'
    elif x>3 or x<=4:
        print('weather is Snow')
        x='weather is Snow'
    elif x>=5:
        print('weather is Fog')
        x='weather is Fog'
    return render_template('weather.html',prediction=x)
if __name__=='__main__':
    app.run(port=8000)