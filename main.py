import uvicorn
from fastapi import FastAPI
from BankNotes import BankNote
import numpy as np
import pandas as pd
import pickle

## create the object call app for the FastAPI class
app = FastAPI()
pickle_in = open('classifier.pkl','rb')
classifier = pickle.load(pickle_in)

## index page
@app.get('/')
def index():
    return {'message':'Hello World'}

@app.post('/predict')
def predict(data:BankNote):
    data = data.dict()
    variance = data['variance']
    skewness = data['skewness']
    curtosis = data['curtosis']
    entropy  = data['entropy']
    prediction = classifier.predict([[variance, skewness, curtosis, entropy]])
    if(prediction[0]<0.5):
        prediction="Its Bank Note"
    else:
        prediction="Its Fake Note"
    return {
        'prediction' : prediction
    }

if __name__ == "__main__":
    uvicorn.run(app, host='127.0.0.1',port='8000')

    #uvicorn main:app --reload