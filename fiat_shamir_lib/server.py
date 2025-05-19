import secrets

class Server:
    """
    Guarda (n, v) p/ cada user. Gera c (challenge) de bits e verifica.
    """

    def __init__(self):
        # Limpando / iniciando logs (opcional)
        self.db = {}  # user_id -> (n, v)

    def register_user(self, user_id, n, v):
        self.db[user_id] = (n, v)

    def send_challenge(self, bits=128):
        """
        Gera um desafio c de bits bits. O desafio é um número aleatório de 128 bits.
        O desafio é gerado usando a função randbits do módulo secrets, que gera um número inteiro aleatório com a quantidade de bits desejada.
        O número gerado é armazenado no log do servidor.
        """
        c = secrets.randbits(bits)
        return c

    #Verifica se y^2 =>  x * v^c mod n
    def verify(self, user_id, x, y, c):
        """
        Verifica se y^2 == x * v^c mod n
        onde:
        - y^2 é o quadrado do valor enviado pelo usuário
        - x é o valor enviado pelo usuário
        - v é o valor público do usuário (armazenado no servidor)
        - c é o desafio enviado pelo servidor
        - n é o módulo (armazenado no servidor)
        """
        user = self.db.get(user_id)
        (n, v) = user
        left = pow(y, 2, n)
        print(f"y^2 = {left}")
        vc = pow(v, c, n)
        right = (x * vc) % n
        print(f"x * v^c mod n = {right}")
        ok = (left == right)

        return ok
