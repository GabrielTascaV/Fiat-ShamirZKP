from fastapi import FastAPI
from pydantic import BaseModel
from fiat_shamir_lib.server import Server

app = FastAPI()
server_instance = Server()

class RegisterData(BaseModel):
    user_id: str
    n: int
    v: int

class VerifyData(BaseModel):
    user_id: str
    x: int
    y: int
    c: int

@app.post("/register")
def register_user(data: RegisterData):
    server_instance.register_user(data.user_id, data.n, data.v)
    return {"message": "User registered successfully"}

@app.get("/challenge/{user_id}")
def get_challenge(user_id: str):
    c = server_instance.send_challenge()
    return {"c": c}

@app.post("/verify")
def verify(data: VerifyData):
    result = server_instance.verify(data.user_id, data.x, data.y, data.c)
    return {"login_success": result}
