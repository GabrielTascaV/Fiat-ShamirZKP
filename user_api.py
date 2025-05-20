from fastapi import FastAPI
from pydantic import BaseModel
import requests
import os
from fiat_shamir_lib.user import User

app = FastAPI()
user_instance = User()
# Classe para os dados de registro
class RegisterRequest(BaseModel):
    user_id: str
    password: str

# Classe para os dados de login
class LoginRequest(BaseModel):
    user_id: str
    password: str

SERVER_URL = os.getenv("SERVER_URL", "http://server_api:8001")
DOMAIN_NAME = os.getenv("DOMAIN_NAME")

# Endpoint para enviar o registro do usuário para o servidor
@app.post("/register")
def register(req: RegisterRequest):
    req.password = req.password + DOMAIN_NAME  # Adiciona o domínio à senha
    user_instance.start_protocol(req.password)
    n = user_instance.get_n()
    v = user_instance.get_public_value_v()

    print(f"v = {v}")

    print(f"Novo cadastro user_id={req.user_id}\n")
    print(f"Senha em texto: {req.password}\n")
    print(f"s (hash) = {user_instance.get_s()}\n")
    print(f"Public v = {v}\n")
    print(f"n = {n}\n\n")
    
    res = requests.post(f"{SERVER_URL}/register", json={
        "user_id": req.user_id,
        "n": n,
        "v": v
    })
    return {"status": res.status_code, "message": "User registered and sent to server."}

# Endpoint para fazer todo o processo de login do usuário
# (desafio, resposta e verificação)
@app.post("/login")
def login(req: LoginRequest):
    x = user_instance.calculate_x()
    req.password = req.password + DOMAIN_NAME  # Adiciona o domínio à senha
    # Log do user
    print(f"Login user_id={req.user_id}\n")
    print(f"Senha em texto (login): {req.password}\n")
    
    challenge = requests.get(f"{SERVER_URL}/challenge", json={
        "user_id": req.user_id,
        "x": x
    }).json()["c"]
    
    y = user_instance.calculate_y(req.password, challenge)
 
    verify_res = requests.post(f"{SERVER_URL}/verify", json={
        "user_id": req.user_id,
        "y": y,
        "c": challenge
    }).json()

    return verify_res
