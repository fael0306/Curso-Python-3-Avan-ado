import random

lista = [1,2,3,4,5,6]

print(random.choice(lista))
print(random.choice(lista))
print(random.choice(lista))
print(random.choice(lista))
print(random.choice(lista))
print(random.choice(lista))

import random

lista = [1,2,3,4,5,6]

print(random.choice(lista))
print(random.choice(lista))
print(random.choice(lista))
print(random.choice(lista))
print(random.choice(lista))
print(random.choice(lista))
print("")
print(random.sample(lista,1))
print(random.sample(lista,2))
print(random.sample(lista,3))
print(random.sample(lista,4))
print(random.sample(lista,5))
print(random.sample(lista,6))
print("")
print(random.randint(0,10))
print(random.randint(0,10))
print(random.randint(0,10))
print(random.randint(0,10))
print(random.randint(0,10))
print(random.randint(0,10))
print(random.randint(0,10))
print(random.randint(0,10))
print(random.randint(0,10))
print(random.randint(0,10))
print("")
random.random()
print("")
random.shuffle(lista)
print(lista)

def multiplicar(x,y):
    "Essa função retorna a multiplicação de 2 números"
    return(x*y)

help(multiplicar)

print(multiplicar.__doc__)

class Teste:
    """Testando a função help"""
    pass

help(Teste)

class p():
    pass

P = p()
print(p.__mro__)
print(p.mro())

class veiculo():
    def __init__(self):
        pass
class carro(veiculo):
    def __init__(self):
        super(carro,self).__init__()
class trem(veiculo):
    pass

print(veiculo.__mro__)
print(carro.__mro__)
print(trem.__mro__)
print(veiculo.mro())
print(carro.mro())
print(trem.mro())

class carrotrem(carro,trem):
    pass

print(carrotrem.__mro__)

# Herança

class Livro(object):
    def __init__(self,nome,conteudo):
        self.nome = nome
        self.conteudo = conteudo

class LivroHTMLMixin(object):
    def renderizar(self):
        return("<html><title>%s</title><body>%s</body></html>") % (self.nome, self.conteudo)

class LivroHTML(Livro, LivroHTMLMixin):
    pass

livro_html = LivroHTML("Algum livro","blablabla")
print(livro_html.renderizar())

def count(n):
    while True:
        yield n
        n = n+1
c = count(0)
print(c)

#c[10:20] -> não funciona

import itertools
for x in itertools.islice(c,10,20):
    print(x)

class A:
    def fazer_algo(self):
        pass
    def outro_metodo(self):
        pass
    def algum_metodo(self,nome):
        print(nome)

class B:
    def __init__(self):
        self.a = A()
    def fazer_algo(self):
        # Delega para self.a
        return self.a.fazer_algo()
    def outro_metodo(self):
        # Delega para self.a
        return self.a.outro_metodo()
    def __getattr__(self, nome):
        return getattr(self.a,nome)

b = B()
b.fazer_algo()
b.algum_metodo("Python")

x = [1,2,3]
y = [4,5,6]
for i,j in zip(x,y):
    print(i,j)

print(list(zip(x,y)))

class Pessoa:
    __slots__ = ["Nome","Idade","Peso"]
    def __init__(self, Nome, Idade, Peso):
        self.Nome = Nome
        self.Idade = Idade
        self.Peso = Peso

pessoa1 = Pessoa("Rafael",22,70)
print(" Nome:",pessoa1.Nome,"\n","Idade:",pessoa1.Idade,"\n","Peso:",pessoa1.Peso)

class SomentePares(list):
    def append(self, inteiro):
        if not isinstance(inteiro, int):
            raise TypeError("Somente inteiros")
        if inteiro%2:
            raise ValueError("Somente pares")

        super().append(inteiro)

numero2 = SomentePares()
#numero2.append(1.77)
numero = SomentePares()
#numero.append(5)
#Caiu na exceção, pois só aceita pares e inteiros
numero2.append(2)
numero2.append(4)
numero.append(6)
numero.append(8)
print(numero)
print(numero2)

def algo():
    raise Exception("Excecao")
    print("depois do raise") # não executa

def algo2():
    try:
        algo()
    except:
        print("Eu peguei uma excecao")
        print("Executado após a exceção")
algo2()

def divisao(divisor):
    try:
        if divisor == 20:
            raise ValueError("Não pode 20")
       # return 10/divisor
    except ZeroDivisionError:
        return "\nDividir por zero não é uma boa ideia"
    except TypeError:
        return "\nDigite um número"
    except ValueError:
        print("Não utilize o número 20")
        raise
    else:
        print("Não ocorreu nenhuma exceção")
    finally:
        print("Isso sempre será executado")

print(divisao(0))
print(divisao("string"))
print(divisao(15))

try:
    raise ValueError("Argumento")
except ValueError as e:
    print("Os argumentos da exceção foram: ", e.args)
finally:
    print("Isso sempre será executado.")

# PEP 8
#import os
#import sys

#obj = minhafuncao(var_one,var_two,
#                  var_three, var_four)

#my_list=[
#    1,2,3,
#    4,5,6,
#    ]

#result = (var1
#          + var2
#         + (var3-var4)
#          - result_var1
#          - result_var4)

#foo ( x, y ) errado
#foo(x,y) correto

#if x==4: print(x)

#PalavrasComecandoPorMaiscula #classe
#minusculas_separadas_por_underscores # função

import json

data = {
    "Nome":"Rafael",
    "Idade": 22,
    "Peso": 62
    }

jsonstr = json.dumps(data)
print(jsonstr)

data = json.loads(jsonstr)
print(jsonstr)
print(type(jsonstr))
print(data)
print(type(data))

print(1+2)
print((1).__add__(2))

class MeuInt(int):
    def __add__(self, num):
        return 0

a = MeuInt(1)
print(a+2)

print(dir(list))
help(list.append)

# Sobrescrevendo um método usando OO
class MinhaLista(list):
    def append(self, *args):
        self.extend(args)

l = MinhaLista()
l.append(1)
l.append(2,3,4,5,6,7)
print(l)

class MyList(list):
    def sort(self):
        return "Opa, você quer ordenar"

lista = [10,5,20]
lista.sort()
print(lista)

lista = MyList()

print(lista.sort()) # Retorna diferente pois está sobrescrito

print(help(list.sort))

#def funcao(*args):
#    print(args)
#funcao(1,2,3,"Rafael")

def funcao(**kwargs):
    print(kwargs)
    
funcao(nome="Rafael",idade=22, linguagem = "Python")

print("")

# ou

def funcao(**kwargs):
    for key, value in kwargs.items():
        print(key,value)
        
funcao(nome="Rafael",idade=22, linguagem = "Python")

for i in "Rafael":
    print(i)

print(sorted("Rafael"))

lista = [i*2 for i in range(1,11)]
print(lista)

class Fibonacci:
    def __init__(self, max):
        self.max = max
    def __iter__(self):
        self.x, self.y = 1,1
        return self
    def __next__(self):
        fib = self.x
        if (fib>self.max):
            raise StopIteration
        self.x, self.y = self.y, self.x+self.y
        return fib

fib = Fibonacci(100)
for i in fib:
    print(i, end=" ")

#__iter__() --> iter(fib)

def fib(max):
    x,y = 1,1
    while x<max:
        yield x
        x,y = y, x+y

gen = fib(15)

'''
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
'''

for i in gen:
    print(i, end=' ')

def somar(a,b):
    return(a+b)

def modificar(funcao):
    def subtrair(a,b):
        return(a-b)
    return subtrair

@modificar
def somar(a,b):
    return (a+b)

print(somar(2,3))

def modificar(funcao):
    def somarpares(a,b):
        if a%2==0 or b%2==0:
            return(a-b)
    return subtrair

print(somar(3,3))
print(somar(2,3))

def meudecorador(funcao):
    def imprimealgo():
        print("Eu não sei somar")
    return imprimealgo

@meudecorador
def imprime():
    print("Eu sei somar")
#imprime=meudecorador(imprime)
imprime()

class MinhaClasse(object):
    var = True

#MinhaClasse = MetaClasse()
#MeuObjeto = MinhaClasse()

MinhaClasse = type("MinhaClasse", (), {"var":True})
print(MinhaClasse)
obj = MinhaClasse()
print(obj.var)

var = 10
print(var.__class__)

nome = "Python"
print(nome.__class__)

class Foo(object): pass

obj = Foo()
print(obj.__class__)

idade = 20
print(idade.__class__)
#Meta Classe
print(idade.__class__.__class__)

class MinhaMetaClasse(type):
    def __new__(cls, clsname, superclasses, attributedict):
        print("clsname: ", clsname)
        print("superclasses: ", superclasses)
        print("atributos: ", attributedict)
        return type.__new__(cls, clsname, superclasses, attributedict)
class Pai:
    pass
class Filha(Pai, metaclass=MinhaMetaClasse):
    pass

obj = Filha()
print(obj.__class__.__class__)

lista = ["Python", "PHP", "C", "Ruby", "Lua"]
print(sorted(lista, key=len))

add = lambda x, y, z: x+y+z
print(add(10,20,30))
print(add("Rafael", " Manteiga", " Balbino"))

x = 10
a = lambda y: x+y
x = 20
b = lambda y: x+y
print(a(10))
print(b(10))
x = 15
print(a(10))
x = 10
a = lambda y, x=x:x+y
x = 20
b = lambda y, x=x:x+y
print(a(10))
print(b(10))

import sqlite3
db = sqlite3.connect("database.db")
c = db.cursor()
c.execute("create table tabela1 (nome text, cod integer, preco real)")
db.commit()
testando = [("Teste",5674,8837),("novamente",222,1200)]
print(testando)

c.executemany("insert into tabela1 values (?,?,?)",testando)
db.commit()
for linha in db.execute("select * from tabela1"):
    print(linha)
# Objetos
#   Atributos (membros de dados)
#   Procedimentos

# objeto carro -> combustível, rodas, acelerar...

# Objetos
#   - representam entidades

# Classes
#   - definem objetos

# Pessoa -> nome, idade, peso, ir_a_escola

# Métodos
#   - representam o comportamento do objeto

"""
class Pessoa(object):
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    def obter_pessoa(self):
        return "<Pessoa (%s,%s)>" % (self.nome, self.idade)

p = Pessoa("Rafael", 28)
print("Tipo do objeto: ", type(p), "\nMemória: ", id(p))
"""
# Polimorfismos embutidos
print(2+3)
print("Rafael"+" Manteiga")

nome = "Rafael"
lista = [1,2,3,4]
tupla = (1,2,3,4)
print(nome[0], lista[0], tupla[0])

class Pai:
    def pai(self):
        print("Oi, sou a classe pai")

class Filha(Pai):
    def filha(self):
        print("Oi, sou a classe filha.")

filha = Filha()
filha.pai()

class Adiciona:
    def __init__(self):
        self.soma = 0
    def adiciona(self, valor):
        self.soma = self.soma+valor

ad = Adiciona()
for i in range(10):
    ad.adiciona(i)

class A(object):
    def a1(self):
        print("a1")

class B(object):
    def b(self):
        print("b")
        A().a1()

objB = B()
objB.b()

class Singleton(object):
    def __new__(cls):
        if not hasattr(cls, "instance"):
            cls.instante = super(Singleton, cls).__new__(cls)
        return cls.instante

s1 = Singleton()
print(s1)
s2 = Singleton()
print(s2)

class Singleton:
    __instance = None
    def __init__(self):
        if not Singleton.__instance:
            print("__init foi chamado")
        else:
            print("Instância já criada: ", self.obter_instancia())

    @classmethod
    def obter_instancia(cls):
        if not cls.__instance:
            cls.__instance = Singleton()
        return cls.__instance

s = Singleton()
print("Objeto criado: ", Singleton.obter_instancia())
s2 = Singleton()

class MinhaClasse:
    __estado_compartilhado = {"1":"2"}
    def __init__(self):
        self.x = 1
        self.__dict__ = self.__estado_compartilhado

b1 = MinhaClasse()
b2 = MinhaClasse()
b1.x = 5
print("b1: ", b1)
print("b2: ", b2)

print(b1.__dict__)
print(b2.__dict__)

a = 5
print(type(a))
print(type(int))

class MetaClasse(type):
    def __call__(cls, *args, **kargs):
        print("Minha metaclasse", args)
        return type.__call__(cls, *args, **kargs)



class int(metaclass=MetaClasse):
    def __init__(self, x, y):
        self.x = x
        self.y = y

obj = int(4, 5)

class MetaSingleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(MetaSingleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]

class Test(metaclass=MetaSingleton):
    pass

t1 = Test()
t2 = Test()

print(t1,t2)

import sqlite3

class MetaSingleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(MetaSingleton, cls).__call__(*args,**kwargs)
        return cls._instances[cls]

class Database(metaclass=MetaSingleton):
    connection = None
    def connect(self):
        if self.connection is None:
            self.connection = sqlite3.connect("database.db")
            self.cursor = self.connection.cursor()
        return self.cursor

db1 = Database().connect()
db2 = Database().connect()

print(db1, db2)


from abc import ABCMeta, abstractmethod

class Animal(metaclass = ABCMeta):
    @abstractmethod
    def som(self):
        pass

class Cachorro(Animal):
    def som(self):
        print("Au au au")
        
class Gato(Animal):
    def som(self):
        print("Meaw meaw meaw")

class Fabrica(object):
    def produzirsom(self, object_type):
        return object_type().som()

if __name__ == "__main__":
    f = Fabrica()
    f.produzirsom(Cachorro)
    f.produzirsom(Gato)

from abc import ABCMeta, abstractmethod

class Secao(metaclass=ABCMeta):
    @abstractmethod
    def descricao(self):
        pass

class SecaoPessoa(Secao):
    def descricao(self):
        print("Seção pessoal")

class SecaoAlbum(Secao):
    def descricao(self):
        print("Seção de fotos")

class SecaoPatente(Secao):
    def descricao(self):
        print("Seção patente")

class SecaoPublicacao(Secao):
    def descricao(self):
        print("Seção publicação")

class Perfil(metaclass=ABCMeta):
    def __init__(self):
        self.secoes = []
        self.criarperfil()

    @abstractmethod
    def criarperfil(self):
        pass
    def obtersecoes(self):
        return self.secoes
    def addsecoes(self, secao):
        self.secoes.append(secao)

class Facebook(Perfil):
    def criarperfil(self):
        self.addsecoes(SecaoPessoa())
        self.addsecoes(SecaoPatente())
        self.addsecoes(SecaoPublicacao())
class Twitter(Perfil):
    def criarperfil(self):
        self.addsecoes(SecaoAlbum())

if __name__=="__main__":
    tipoperfil = "Facebook"
    perfil = eval(tipoperfil)()
    print(perfil.obtersecoes())

