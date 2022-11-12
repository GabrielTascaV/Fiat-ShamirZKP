import random

class Servidor:
    def _init_(self):
        self.senhaUsuario = 0
        self.calculoSenha = 0

    def register_server(self,r,n):
        func_registro = (r ** 2) % n
        self.calculoSenha = func_registro

    def send_challenge():
        return random.randint(0,1)

    def get_calculo(self):
        return self.calculoSenha

    def verifica(x,y,v,c,n):
        print(y)
        y_quad = y ** 2
        print(y_quad)
        calculo = (x * (v ** c)) % n
        print("calculo = ", calculo)
        if y_quad == calculo:
            return True
        else:
            return False

class Usuario:
    def _init_(self):
        self.senhaUsuario = 0

    def set_senha(self,s):
        self.senhaUsuario = s

    def register_user(self,url):
        s = hash(self.senhaUsuario+url)
        if(s<0):
            s = -(s)
        self.senhaUsuario = s

    def get_senha(self):
        return self.senhaUsuario

    def solve_challenge(self, c, n, r):
        return r


def get_primo():
    x = random.randint(2,50)
    for i in range(2,x):
        if(x % i == 0):
            return get_primo()
    else:
        return x
    
def get_n():
    p = get_primo()
    q = get_primo()
    return p * q

def calcula_v(s,n):
    return (s ** 2) % n

def calcula_y(r,s,c,n):
    return (r * (s ** c)) % n


#Criando o Verificador, Provador, N, R e senha
user = Usuario
server = Servidor
# n = get_n()
# r = random.random()
# url = "localhost::8080"
# u._init_(u)
# s._init_(s)
# u.set_senha(u,"secreto")
# #----------------------------------------
# #Calculando V = S^2 mod N
# u.register_user(u,url)
# v = calcula_v(u.get_senha(u),n)
# #Escolhendo o R e Calculando x = r^2 mod N
# s.register_server(s,r,n)

# #Enviando desafio
# c = s.send_challenge()
# print(c)

# #Calculando Y

# y = calcula_y(r,u.get_senha(u),c,n)

# #Verificando se esta correto

# print(s.verifica(s,y,v,c,n))

n = 35
s = 16
v = calcula_v(s,n)
print("v = ", v)

r = 10
x = calcula_v(r,n)
print("x = ", x)
c = 0
y = calcula_y(r,s,c,n)
print("y = ", y)
print(server.verifica(x,y,v,c,n))
#----------------------------------TODO: CONGRUENCIA EM PYTHON -------------------------------------------------