from flask import Flask,render_template,request
import pickle
import numpy as np
import pandas as pd
app=Flask(__name__)
model=pickle.load(open('model.pkl','rb'))
@app.route('/')
def loan():
    return render_template('loan.html')
@app.route('/predict',methods=['post'])
def predict():
    Education=int(request.values['Education'])
    print("Education",Education)
    Self_Employed=int(request.values['Self_Employed'])
    print("Self_Employed",Self_Employed)
    ApplicantIncome=int(request.values['ApplicantIncome'])
    print("ApplicantIncome",ApplicantIncome)
    LoanAmount=int(request.values['LoanAmount'])
    print("LoanAmount",LoanAmount)



    data=[[Education,Self_Employed,ApplicantIncome,LoanAmount]]
    df=pd.DataFrame(data,columns=['Education','Self_Employed','ApplicantIncome','LoanAmount'])
    a=model.predict(df)
    print(a)
    if a==0:
        print('Rejected')
        x='Rejected'
    else:
        print('Approved')
        x='Approved'
    return render_template('loan.html',prediction=x)
if __name__=='__main__':
    app.run(port=8000)