from fastapi import FastAPI

app = FastAPI()

@app.get("/home")
def hello():
    return {"message": "This is Home page..."}

@app.get("/about")
def about():
    return {"message": "This is About Us page..."}