##import the package

import uvicorn
from fastapi import FastAPI

## create the object call app for the FastAPI class
app = FastAPI()

## index page
@app.get('/')
def index():
    return {'message':'Hello World'}

@app.get('/welcome')
def welcome(name:str,age:int):
    msg= f"Hello {name},Welcome to the Fast API leaning. Your Age is {age}"
    return {'message':msg}

### main function
if __name__=='__main__':
    uvicorn.run(app, host='127.0.0.1',port='8000')

#Running the script
#uvicorn filename:object name --reload
#uvicorn SmipleFastApi:app --reload

