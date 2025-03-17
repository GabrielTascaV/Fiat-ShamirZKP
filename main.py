import random

# Importa as classes
from User import User
from Server import Server

# -----------------------------------------
# FUNÇÕES AUXILIARES
# -----------------------------------------
def get_primo():
    """Gera aleatoriamente um 'primo' pequeno, apenas fins didáticos."""
    x = random.randint(2, 50)
    for i in range(2, x):
        if x % i == 0:
            return get_primo()
    else:
        return x

def get_n():
    """
    Gera n = p*q, com p e q retornados por get_primo().
    Lembrando que aqui p e q são muito pequenos
    e não servem para segurança real.
    """
    p = get_primo()
    q = get_primo()
    return p * q

def calcula_v(s, n):
    """Retorna s^2 mod n."""
    return pow(s, 2, n)

def calcula_y(r, s, c, n):
    """
    Gera a resposta y ao desafio c.
    Se c=0 => y = r,
    se c=1 => y = (r*s) mod n.
    """
    if c == 0:
        return r
    else:
        return (r * s) % n

# -----------------------------------------
# FLUXO DE CADASTRO E LOGIN
# -----------------------------------------
def cadastro_usuario(n, url, user, server):
    senha = input("Digite sua senha de cadastro: ")
    # Guarda senha "em bruto" no objeto Usuario
    user.set_senha(senha)
    # Faz register_user: cria s = hash(senha+url) e set_senha no servidor
    user.register_user(url, server)

    print("\nSenha armazenada no servidor:", server.get_senha())
    # Observação: Em um Fiat-Shamir completo, o servidor guardaria
    # v = s^2 mod n, mas aqui o código está simplificado.

def log_in(user, n, v, server, url):
    nova_senha = input("Digite sua senha para log in: ")
    user.set_senha(nova_senha)
    user.register_user(url, server)

    accept = 0
    # Roda 5 vezes (cada vez gerando r, c e testando)
    for i in range(5):
        r = random.randint(1, 100)
        x = pow(r, 2, n)  # x = r^2 mod n
        c = server.send_challenge()
        # Gera y
        # (no solve_challenge está retornando r, mas poderia ser sofisticado)
        y = calcula_y(r, user.get_senha(), c, n)

        # Verifica
        if server.verifica(x, y, v, c, n):
            accept += 1
        else:
            print("Senha errada na rodada", i+1)
            break

    if accept == 5:
        print("Log in foi um sucesso!")
    else:
        print("Falha no log in.")

# -----------------------------------------
# MAIN
# -----------------------------------------
def main():
    # Instancia um Usuario e um Servidor
    user = User()
    server = Server("google.com")

    # Cria n
    n = get_n()

    print("---- CADASTRO ----")
    cadastro_usuario(n, "google.com", user, server)

    # Em um Fiat-Shamir real, o servidor guardaria v = s^2 mod n
    # No código original, user.get_senha() já está transformada
    v = calcula_v(user.get_senha(), n)
    print("Cadastro concluído. Valor v =", v)

    print("\n---- LOGIN ----")
    log_in(user, n, v, server, "google.com")

if __name__ == "__main__":
    main()
