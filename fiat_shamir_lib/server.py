import secrets

class Server:
    """
    Guarda (n, v, lastX) p/ cada user. Gera c (challenge) de bits e verifica.
    """

    def __init__(self):
        # Limpando / iniciando logs (opcional)
        self.db = {}  # user_id -> (n, v, lastX)

    def register_user(self, user_id, n, v, lastX=None):
        """
        Armazena (n, v) p/ cada user_id.
        O valor de n é o módulo e v é o valor público do usuário.
        O valor de lastX é o último valor de x gerado pelo usuário.
        O valor de lastX é usado para verificar se o usuário está tentando fazer login com o mesmo valor de x.
        """
        self.db[user_id] = (n, v, lastX)

    def send_challenge(self, user_id, x, bits=256):
        """
        Gera um desafio c de bits bits. O desafio é um número aleatório de 128 bits.
        O desafio é gerado usando a função randbits do módulo secrets, que gera um número inteiro aleatório com a quantidade de bits desejada.
        O número gerado é armazenado no log do servidor.
        """
        (n,v, lastX) = self.db.get(user_id)
        lastX = x
        self.db[user_id] = (n, v, lastX)
        c = secrets.randbits(bits)
        return c

    #Verifica se y^2 =>  x * v^c mod n
    def verify(self, user_id, y, c):
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
        (n, v, x) = user
        left = pow(y, 2, n)
        print(f"y^2 = {left}")
        vc = pow(v, c, n)
        right = (x * vc) % n
        print(f"x * v^c mod n = {right}")
        ok = (left == right)

        return ok
