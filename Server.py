import random

class Server:
    def __init__(self, url):
        self.senhaUsuario = 0
        self.urlSite = url
        self.calculoSenha = 0  # opcional, caso queira armazenar internamente

    def set_senha(self, senha):
        """Armazena localmente a 'senha' processada do usuário."""
        self.senhaUsuario = senha

    def get_senha(self):
        """Retorna a 'senha' (aqui representada como s ou outro valor)."""
        return self.senhaUsuario

    def register_server(self, r, n):
        """
        Registra r^2 mod n só para fins de demonstração,
        representando 'x = r^2 mod n' do protocolo.
        """
        func_registro = (r ** 2) % n
        self.calculoSenha = func_registro

    @staticmethod
    def send_challenge():
        """
        Retorna um desafio c (0 ou 1). Em um Fiat-Shamir real,
        poderia ter mais bits.
        """
        return random.randint(0, 1)

    def get_calculo(self):
        """
        Retorna o valor de calculoSenha (r^2 mod n) se precisarmos.
        """
        return self.calculoSenha

    @staticmethod
    def verifica(x, y, v, c, n):
        """
        Verifica se y^2 equivale a x * (v^c) (mod n).
        x = r^2 mod n
        y = r * s^c mod n (teoricamente)
        v = s^2 mod n (valor público)
        c = 0 ou 1
        """
        y_quad = (y ** 2) % n
        calculo = (x * pow(v, c, n)) % n
        return (y_quad == calculo)
