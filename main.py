from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def index():
    return {"data":{"ids":[1,2,3,4,5]}}

@app.get('/about')
def about():
    return {"data":"This is about page!"}