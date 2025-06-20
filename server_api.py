from fastapi import FastAPI
from pydantic import BaseModel
from fiat_shamir_lib.server import Server
import os

app = FastAPI()
server_instance = Server()
DOMAIN_NAME = os.getenv("DOMAIN_NAME")

# Classe para os dados de registro
class RegisterData(BaseModel):
    user_id: str
    n: int
    v: int

# Classe para o request de challenge
class ChallengeData(BaseModel):
    user_id: str
    x: int

# Classe para os dados de verificação
class VerifyData(BaseModel):
    user_id: str
    y: int
    c: int

# Endpoint para registrar um usuário
@app.post("/register")
def register_user(data: RegisterData):
    server_instance.register_user(data.user_id, data.n, data.v)
    # Log do servidor
    print(f"Servidor={DOMAIN_NAME}\n")
    print(f"Novo cadastro user_id={data.user_id}\n")
    print(f"Public v = {data.v}\n")
    print(f"Public n = {data.n}\n\n")
    return {"message": "User registered successfully"}

# Endpoint para enviar o desafio para o usuário
@app.get("/challenge/")
def get_challenge(data: ChallengeData):
    c = server_instance.send_challenge(data.user_id, data.x)
    # Log do servidor
    print(f"Desafio enviado para Usuário={data.user_id}: c={c}\n")
    return {"c": c}

# Endpoint para verificar o resultado do desafio
@app.post("/verify")
def verify(data: VerifyData):
    result = server_instance.verify(data.user_id, data.y, data.c)
    # Log do servidor
    print(f"Verificação user_id={data.user_id}, \ny={data.y}, \nc={data.c}, \nresultado={result}\n")
    return {"login_success": result}
