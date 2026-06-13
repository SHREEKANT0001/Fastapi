from fastapi import FastAPI

app=FastAPI()

@app.post("/create_user")
def create_user(name:str,age:int,college:str,roll_no:str):
    return{
        "message":"user created",
        "data": {
            "name":name,
            "age":age,
            "college":college,
            "roll no":roll_no
        }
    }