import hashlib
import secrets
from Crypto.Util import number
import os

class UserReal:
    """
    O 'usuário' guarda:
      - n (produto de 2 primos grandes)
      - s (segredo, derivado da senha)
      - r (valor aleatório, usado para gerar x e y)
    """

    def __init__(self):
        with open("fiat_shamir_lib/logs/usuarios_log.txt", "w", encoding="utf-8") as f:
            f.write("=== LOG DE USUARIOS ===\n")
        # Produto de 2 primos
        self.n = None
        # Senha armazenada em formato de hash
        self.s = None
        # Valor aleatório
        self.r = None

    def start_protocol(self, pass_str, bits=1024):
        """
        1) Gera p, q => n = p*q (bits ~ 1024)
        2) Converte pass_str -> s via SHA-256 (mod n)
        3) Garante gcd(s, n)=1
        """
        # Gera primos
        p = number.getPrime(bits // 2)
        q = number.getPrime(bits // 2)
        self.n = p * q

        # Transforma string de UTF-8 para bytes e aplica SHA-256 e retorna os 32 bytes
        digest = hashlib.sha256(pass_str.encode('utf-8')).digest()
        # Converte os 32 bytes para um inteiro e aplica mod n para garantir que fica em entro de 0 e n-1
        candidate_s = int.from_bytes(digest, 'big') % self.n

        i = 0
        # Como usamos aritimética modular, garantimos que o gcd(s, n) = 1 para que possamos fazer as operações de inversão modular
        while number.GCD(candidate_s, self.n) != 1 or candidate_s <= 1:
            i += 1
            extra = hashlib.sha256(digest + i.to_bytes(4, 'big')).digest()
            candidate_s = int.from_bytes(extra, 'big') % self.n

        self.s = candidate_s

    def calculate_x(self):
        """
        Gera x = r^2 mod n
        """
        # Maneira de aleatorizar o R sem que seja <= 1 para nao deixar o desafio trivial
        while True:
            self.r = secrets.randbelow(self.n)
            if self.r > 1:
                break
        # Calcula x = r^2 mod n
        x = pow(self.r, 2, self.n)
        return x

    def calculate_y(self, pass_login, c):
        """
        Gera y = r * s^c mod n
        """
        # Transforma string de UTF-8 para bytes e aplica SHA-256 e retorna os 32 bytes
        digest = hashlib.sha256(pass_login.encode('utf-8')).digest()
        # Converte os 32 bytes para um inteiro e aplica mod n para garantir que fica em entro de 0 e n-1
        candidate_s = int.from_bytes(digest, 'big') % self.n

        # Calcula y = r * s^c mod n
        y = (self.r * pow(candidate_s, c, self.n)) % self.n
        print(f"y = {y}")
        return y

    def get_public_value_v(self):
        return pow(self.s, 2, self.n)
    
    def get_n(self):
        return self.n

    def get_s(self):
        return self.s
