import secrets
import os
from fiat_shamir_lib.user import UserReal
from fiat_shamir_lib.server import ServerReal

def main():

    user = UserReal()
    server = ServerReal()

    user_id = "usuario1"

    # 1) CADASTRO
    senha_cadastro = input("Digite sua senha para CADASTRO: ")
    user.start_protocol(senha_cadastro, bits=1024)
    n = user.get_n()
    v = user.get_public_value_v()

    # Grava o cadastro no log de usuários
    with open("fiat_shamir_lib/logs/usuarios_log.txt", "a", encoding="utf-8") as f:
        f.write(f"Novo cadastro user_id={user_id}\n")
        f.write(f"Senha em texto: {senha_cadastro}\n")
        f.write(f"s (hash) = {user.get_s()}\n")
        f.write(f"Public v = {v}\n")
        f.write(f"n = {n}\n\n")

    # Registra no servidor
    server.register_user(user_id, n, v)
    print(f"Cadastro concluído.")

    # 2) LOGIN
    senha_login = input("\nDigite sua senha para LOGIN: ")

    # Log do user
    with open("fiat_shamir_lib/logs/usuarios_log.txt", "a", encoding="utf-8") as f:
        f.write(f"Login user_id={user_id}\n")
        f.write(f"Senha em texto (login): {senha_login}\n")
        f.write(f"S = {user.get_s()}\n\n")

    # Realiza K rodadas, precisa de K rodadas?
    K = 3
    success = True

    for i in range(K):
        x = user.calculate_x()

        # Pede challenge ao servidor
        c = server.send_challenge(bits=128, log_file="fiat_shamir_lib/logs/server_log.txt")

        y = user.calculate_y(senha_login,c)

        # Verifica
        ok = server.verify(user_id, x, y, c, log_file="fiat_shamir_lib/logs/server_log.txt")
        print(f"Rodada {i+1}: ", "OK" if ok else "Falhou")
        if not ok:
            success = False
            break

    if success:
        print("\nLogin bem-sucedido!")
    else:
        print("\nFalha na autenticação.")

if __name__ == "__main__":
    main()
