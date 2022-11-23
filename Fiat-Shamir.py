import random

class Servidor:
    def _init_(self,url):
        self.senhaUsuario = 0
        self.urlSite = url

    def set_senha(self,senha):
        self.senhaUsuario = senha
    def get_senha(self):
        return self.senhaUsuario    

    def register_server(self,r,n):
        func_registro = (r ** 2) % n
        self.calculoSenha = func_registro

    def send_challenge():
        return random.randint(0,1)

    def get_calculo(self):
        return self.calculoSenha

    def verifica(x,y,v,c,n):
        y_quad = y ** 2
        calculo = (x * (v ** c)) % n
        y_mod = y_quad % n
        calc_mod = calculo % n
        if y_mod == calculo:
            return True
        else:
            return False

class Usuario:
    def _init_(self):
        self.senhaUsuario = 0

    def set_senha(self,s):
        self.senhaUsuario = s

    def register_user(self,url,server:Servidor):
        s = hash(self.senhaUsuario+url)
        if(s<0):
            s = -(s)
        self.senhaUsuario = s
        server.set_senha(server,s)
        

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
    if(c == 0):
        return r
    else: 
        y = (r * s) % n
        return y

def cadastro_usuario(n,url,user,server):
    #Digita a senha
    senha = input("Digite sua senha de cadastro: ")
    user.set_senha(user,senha)
    #transforma a senha e url em um Hash e armazena
    user.register_user(user,url,server)
    print("")
    print("Senha armazenada no servidor: ", server.get_senha(server))

def log_in(user,n,v,server,url):
    #Digita a senha de Log-In
    nova_senha =input("Digite sua senha para log in: ")
    user.set_senha(user,nova_senha)
    user.register_user(user,url,server)
    accept = 0
    #Faz o loop 5 vezes pois caso Challenge de 0 de primeira não faria sentido o teste
    for i in range(0,5):
        #Seleciona um Int Aleatorio
        r = random.randint(1,100)
        #Calculo X = r^2 mod N
        x = calcula_v(r,n)
        #Envia o Challenge que pertence à {0,1}
        c = server.send_challenge()
        # Calcula Y = r * S^C mod C 
        y = calcula_y(r,user.get_senha(user),c,n)
        #Faz a verificação se são iguais
        if(server.verifica(x,y,v,c,n) == True):
            accept += 1
        else:
            print("Senha errada")
            break
    #Verifica se todos deram corretos
    if(accept == 5):
        print("Log in foi um sucesso")



#Criando o Verificador, Provador, N, R e senha
user = Usuario
url1 = "google.com"
url2 = "facebook.com"
server1 = Servidor
server1._init_(server1,url1)
server2 = Servidor
server2._init_(server2,url1)
#Criando N com multiplicação de primos
n = get_n()


#-------------- SERVER 1------------------------
#Função de cadastro
print("Cadastro site 1: (url: google.com)")
cadastro_usuario(n,url1,user,server1)
#Faz o calculo de V = S^2 mod N
v1 = calcula_v(user.get_senha(user),n)
print("Cadastro no Google realizado com sucesso")
print("")
print("")


#--------------- SERVER 2 ---------------------
#Função de cadastro
print("Cadastro site 2: (url: facebook.com)")
cadastro_usuario(n,url2,user,server2)
#Faz o calculo de V = S^2 mod N
v2 = calcula_v(user.get_senha(user),n)
print("Cadastro no Facebook realizado com sucesso")

# ---------------------LOG IN---------------------
print("")
print("")
print("LOG IN FACEBOOK")
log_in(user,n,v1,server1,url1)
print("")
print("")
print("LOG IN GOOGLE")
log_in(user,n,v2,server2,url2)
# ------------------------------------------------
def exemplo_peggy_1():
    server = Servidor
    n = 35
    s = 16
    v = calcula_v(s,n)
    print("V: ", v)
    r = 10
    x = calcula_v(r,n)
    print("X: ", x)
    c = 0
    y = calcula_y(r,s,c,n)
    print("Y: ", y)
    ver = server.verifica(x,y,v,c,n)
    print("Verifica: ", ver)


# print("Exemplo Peggy 1")
# exemplo_peggy_1()

def exemplo_peggy_2():
    server = Servidor
    n = 35
    s = 16
    v = calcula_v(s,n)
    print("V: ", v)
    r = 20
    x = calcula_v(r,n)
    print("X: ", x)
    c = 1
    y = calcula_y(r,s,c,n)
    print("Y: ", y)
    ver = server.verifica(x,y,v,c,n)
    print("Verifica: ", ver)

# print("Exemplo Peggy 2")
# exemplo_peggy_2()