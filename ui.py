import requests

def escolher_api():
    dominio = input("Digite o domínio (poa ou pucrs): ").strip()
    if dominio == "poa":
        return "http://172.17.8.9:8000"
    elif dominio == "pucrs":
        return "http://172.17.8.9:8002"
    else:
        print("Domínio inválido.")
        return escolher_api()

def cadastrar_usuario():
    global USER_API_URL
    USER_API_URL = escolher_api()

    user_id = input("Digite o user_id para cadastro: ")
    senha = input("Digite a senha: ")

    response = requests.post(f"{USER_API_URL}/register", json={
        "user_id": user_id,
        "password": senha
    })

    if response.status_code == 200:
        print("Usuário cadastrado com sucesso.")
    else:
        print(f"Erro ao cadastrar: {response.text}")

def fazer_login():
    USER_API_URL = escolher_api()

    user_id = input("Digite o user_id para login: ")
    senha = input("Digite a senha: ")

    response = requests.post(f"{USER_API_URL}/login", json={
        "user_id": user_id,
        "password": senha
    })

    if response.status_code == 200:
        resultado = response.json()
        if resultado.get("login_success"):
            print("Login bem-sucedido!")
        else:
            print("Falha no login. Credenciais inválidas.")
    else:
        print(f"Erro no login: {response.text}")

def main():
    while True:
        print("\n=== MENU ===")
        print("1. Cadastrar usuário")
        print("2. Fazer login")
        print("3. Sair")
        opcao = input("Escolha uma opção (1, 2 ou 3): ")

        if opcao == "1":
            cadastrar_usuario()
        elif opcao == "2":
            fazer_login()
        elif opcao == "3":
            print("Encerrando o programa.")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()