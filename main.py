from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Welcome FastAPI"}

@app.get("/about")
def about():
    return{"this website is about e commerce"}

@app.get("/contact")
def contact():
    return{"contact":"you can contact us on linkedin"}

@app.get("/policy")
def policy():
    return{"policy:accept the terms and condition"}