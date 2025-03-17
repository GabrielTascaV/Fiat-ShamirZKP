import hashlib

class User:
    def __init__(self):
        self.senhaUsuario = 0  # inteiro que representará a versão final em bytes

    def set_senha(self, s):
        """Define a senha (string em texto) internamente só como string crua."""
        self.senhaUsuario = s

    def get_senha(self):
        """Retorna o valor inteiro já convertido."""
        return self.senhaUsuario

    def register_user(self, url, server):
        """
        Faz a transformação da senha em bytes + url, para um valor inteiro.
        Em vez de usar hash() nativo, usamos SHA-256 para termos bytes e um valor previsível.
        """
        # Concatena senha + url em bytes
        #    Se a self.senhaUsuario ainda for int, talvez precise cast p/ string, etc.
        senha_str = str(self.senhaUsuario)  # caso queira forçar se for int
        concat_bytes = (senha_str + url).encode('utf-8')

        # Faz o SHA-256 => digest de 32 bytes
        digest = hashlib.sha256(concat_bytes).digest()

        # Converte esses 32 bytes em inteiro (big-endian, sem sinal)
        s_val = int.from_bytes(digest, byteorder='big', signed=False)

        # Armazena s_val como 'senhaUsuario' (inteiro)
        self.senhaUsuario = s_val

        # Chama o set_senha do servidor, passando esse int
        server.set_senha(s_val)

    def solve_challenge(self, c, n, r):
        """
        Exemplo didático igual antes: retorna r.
        No Fiat-Shamir real, ficaria y = r * s^c mod n,
        mas aqui mantemos a lógica simples.
        """

        y = r * pow(self.senhaUsuario, c, n)
        return y
