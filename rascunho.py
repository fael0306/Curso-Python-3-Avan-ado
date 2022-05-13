x,y,z = [1,2,3]
n1,n2 = ("marcos","joao")
a,b,c,d,e = "hello"
x,y,_ = [1,2,3]
_,x,y = [1,2,3]
lista = [9,4,5,15,20]
*n1, n2 = lista
n1,*n2 = lista
notas = [9,7,8,5,10,20,30]
n1,*n2,n3 = notas
n1,*_,n3 = notas
gerador = (letra for letra in "python")
print(next(gerador))
print(next(gerador))
print(next(gerador))
print(next(gerador))
print(next(gerador))
print(next(gerador))
def gerador2():
    for i in range(5):
        yield i
g = gerador2()
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))

from collections import deque

fila = deque(maxlen=4)
fila.append(1)
fila.append(2)
fila.append(3)
fila.append(4)
fila.append(5)
print(fila)

f = deque()
f.append(1)
f.append(2)
f.append(3)
f.appendleft(4)
print(f)

f.pop()
print(f)
f.popleft()
print(f)

import heapq
idades = [15,10,20,18,25,8,19]
menores3idades = heapq.nsmallest(3,idades)
maiores3idades = heapq.nlargest(3,idades)
heapq.heapify(idades)
heapq.heappop(idades)
heapq.heappop(idades)
heapq.heappop(idades)
heapq.heappush(idades,8)

class PriorityQueue:
    def __init__ (self):
        self._queue = []
        self._index = 0
    def push(self,item,priority):
        heapq.heappush(self._queue, (-priority, self._index, item))
        self._index = self._index+1
    def pop(self):
        return heapq.heappop(self._queue)[-1]

class pessoa:
    def __init__(self,nome,idade):
        self.nome = nome
        self.idade = idade
    def __repr__(self): 
        return self.nome

q = PriorityQueue()
q.push(pessoa('Rafael',22),22)
q.push(pessoa('Gabriel',22),50)
q.push(pessoa('Carlos',50),34)
q.push(pessoa('Maria',35),55)

print(q.pop())


from operator import xor

n1 = 5
n2 = 9
b1 = bin(n1)
b2 = bin(n2)
r = n1^n2
n1 << 2
r = (~n1) #Complemento

lista = [10,11,3,20,18,7,9]
lista = sorted(lista)

tupla = ['Rafael','Gabriel','Fernando']
tupla = sorted(tupla)

d = {1:'b', 2:'a',3:'c'}
d = sorted(d)

def pelonome(pessoa):
    return pessoa.nome
    
def pelaidade(pessoa):
    return pessoa.idade

p1 = pessoa('Rafael',22)
p2 = pessoa('Gabriel',22)
p3 = pessoa('Diego',38)

pessoas = [p1,p2,p3]
print(sorted(pessoas,key = pelonome))
print(sorted(pessoas,key = pelaidade))

def pai(num):
    def filho1():
        print("Sou o filho1")
    def filho2():
        print("Sou o filho2")
    try:
        assert num == 20
        return filho1
    except AssertionError:
        return filho2

f1 = pai(10)
f2 = pai(20)

f1()
f2()

from collections import defaultdict
d = defaultdict(list)
d['rafael'].append(10)
d['rafael'].append(20)
d['rafael'].append(30)
d['joao'].append(1)
d['joao'].append(2)
print(d['joao'])
d = defaultdict(set)
d['rafael'].add(30)
d['rafael'].add(30)
d['rafael'].add(30)
d['rafael'].add(0)

from collections import OrderedDict

d = OrderedDict()

d['Python'] = 10
d['Java'] = 5
d['PHP'] = 6
d['C'] = 10

for key in d:
    print(key, d[key])
    
d2 = {}

d2['Python'] = 10
d2['Java'] = 5
d2['PHP'] = 6
d2['C'] = 10

print(d2)

from collections import Counter

c = Counter(a=4,b=2,c=3)
c.elements()

lista = list(c.elements())

print(lista)

lista = [1,2,3,4,5,6]
a = lista[-1]
b = lista[-2]
c = lista[-3]
d = lista[-4:-2]
e = lista[::-2]

print(a)
print(b)
print(c)
print(d)
print(e)

lista = [1,2,3,4,5,6]

ultimostres = slice(-3,None)

a = lista[ultimostres]

print(a)

c = {1,2,3,4,5}

d = {3,3,4,4,6,7}

print(c)
print(d)

uniao = c | d

print(uniao)

intersecao = c & d

print(intersecao)

uu = c-d

print(uu)

aa = c^d

print(aa)

import itertools

for p in itertools.product([1,2,3],[4,5]):
    print(p)
    
import itertools

for p in itertools.permutations([1,2,3]):
    print(''.join(str(x) for x in p))
    
    
d = {'marcos':28,'joao':19,'maria':25}

a = d['marcos']

print(d.get('joao'))


if d.get('Teste'):
    print("Chave existente")
else:
    print("chave inexistente")
    
    
import itertools

l1 = [1,2,3]
l2 = [4,5,6]

comb = itertools.chain(l1,l2)

print(list(comb))

l3 = ["Rafael","Gabriel","Python"]

comb = itertools.chain(l1,l2,l3)

print(list(comb))

combinando = zip([1,2,3],[4,5,6])
# Devolve um objeto

# Transformando objeto em lista
r = list(combinando)

print(r)

from operator import itemgetter
from itertools import groupby

exemplos = [("Marcos",28),("Pedro",19),("João",20),("Marcos",20),("João",18),("Marcos",30)]

exemplos.sort(key=itemgetter(0))

print({key: sorted(map(itemgetter(1),value)) for key, value in groupby(exemplos,key=itemgetter(0))})

tupla = (1,2,3,4)
for count, elem in enumerate(tupla):
    print('%d %d'% (count,elem))

d = {'PC':3000,'Fone de ouvido':100,'Iphone':5000}

menorpreco = min(zip(d.values(), d.keys()))
maiorpreco = max(zip(d.values(), d.keys()))

a = min(d.values())
b = max(d.values())
c = min(d.keys())
d = max(d.keys())

d = {'Marcos':28,'Rafael':19,'Janderson':20,'Milena':20,'João':18,'Marcos':30}

d2 = {'José':18,'Marcos':25,'Rafael':22,'Gabriel':22,'Jeferson':18,'Fabrício':30}

a=d.keys()
b=d2.keys()

c = d.keys() & d2.keys()

print(c)

ex = d.keys() - d2.keys()

print(ex)

e = d.values()
f = d2.values()

print(e)
print(f)

from collections import Counter

palavras = ['Rafael','Gabriel','Isabella','Maria','Gertrudes','Rafael','Gabriel','Adriano','Rafael','Gabriel']

palavrascont = Counter(palavras)

maiscomum = palavrascont.most_common(1)
duasmaiscomuns = palavrascont.most_common(2)
tresmaiscomuns = palavrascont.most_common(3)

print(maiscomum)
print(duasmaiscomuns)
print(tresmaiscomuns)
#etc.

from collections import Counter

a = Counter([1,1,2,3,4,4,5,6])
b = Counter([2,2,1,3,5,6,7])

print(a)
print(b)

c = a+b

print(c)

linhas = [{'Nome':'Rafael','Idade':22},
          {'Nome':'Gabriel','Idade':22},
          {'Nome':'Carlos','Idade':55},
          {'Nome':'Isabel','Idade':59},
          {'Nome':'Isabel','Idade':58}]

print(linhas)

from operator import itemgetter

linhaspelonome = sorted(linhas,key=itemgetter('Nome'))
linhaspelaidade = sorted(linhas,key=itemgetter('Idade'))

print(linhaspelonome)
print(linhaspelaidade)

ordem = sorted(linhas,key=itemgetter('Nome','Idade'))

print(ordem)

from operator import itemgetter

lista = [{'idade':28},{'idade':15},{'idade':20}]

menor = min(lista,key=itemgetter('idade'))
maior = max(lista,key=itemgetter('idade'))

print(menor)
print(maior)

class Objeto:
    def __init__(self, obj_id):
        self.obj_id = obj_id
    def __repr__(self):
        return str(self.obj_id)

objetos = [Objeto(90), Objeto(15), Objeto(20)]
print(objetos)

objetos = sorted(objetos, key = lambda obj: obj.obj_id)
print(objetos)


from operator import attrgetter

objetos = sorted(objetos, key = attrgetter('obj_id'))
print(objetos)

from operator import itemgetter
from itertools import groupby

linhas = [
    {'Produto':'Calça','Preço':300},
    {'Produto':'Bermuda','Preço':120},
    {'Produto':'Camisa','Preço':120},
    {'Produto':'Casaco','Preço':300},
    {'Produto':'Tênis','Preço':120}
    ]

linhas.sort(key=itemgetter('Preço'))

for data, items in groupby(linhas, key=itemgetter('Preço')):
    print(data)
    for i in items:
        print(' ', i)

lista = [10,-5,20,30,-40,100]

a = [i for i in lista if i>0]
b = [i for i in lista if i<0]

print(a)
print(b)

p = (i for i in lista if i>0)
print(p)

for j in p:
    print(j)

lista = [1,2,3,4]

import math

quadrado = [round(math.sqrt(i),2) for i in lista if i>=3]
print(quadrado)

from itertools import compress

nomes = ['Rafael','Gabriel','Maria','Pedro']
cont = [10,5,6,2]
mais5 = [i>5 for i in cont]
lista = list(compress(nomes,mais5))
print(lista)


precos = {
    'Iphone':2500,
    'Notebook':2000,
    'Mouse':90,
    'Teclado':70
    }

precosmais100 = {key:value for key, value in precos.items() if value>100}

print(precosmais100)

from collections import namedtuple

Subscriber = namedtuple('Subscriber', ['id', 'email'])

sub = Subscriber('1000','rafael.manteiga@hotmail.com')

print(sub.id)
print(sub.email)

len(sub)

id, email = sub
print(id)
print(email)

lista = [10,5,20,8]
s = sum(lista)
m = max(lista)
m2 = min(lista)

print(s)
print(m)
print(m2)

lista = [1100,900,320]

soma_quad = sum([x*x for x in lista])
print(soma_quad)

soma_quad = sum(x*x for x in lista)
print(soma_quad)

a = {'x':1, 'z':3}
b = {'y':2, 'z':4}

from collections import ChainMap

c = ChainMap(a,b)
print(c)
print(c['x'])
print(c['y'])
print(c['z']) # Chave duplicada: vale o primeiro mapeamento

print(len(c))

del c['x']
print(a)

a = {'x':1,'z':3}

merged = dict(b)
merged.update(a)

print(merged['x'])
print(merged['y'])
print(merged['z'])

s = 'arquivo.txt'
a = s.endswith('.txt')
print(a)
b = s.startswith('arq')
print(b)
c = s.startswith('xxx')
print(c)

from fnmatch import fnmatch,  fnmatchcase

a = fnmatch('qrquivo.txt,','*.txt')
print(a)

b = fnmatch('arquivo.py','*.txt')
print(b)

c = fnmatch('arq10.txt','arq[0-9]*')
print(c)

d = fnmatchcase('arquivo.txt','*.TXT')
print(d)

texto = 'arquivo.txt'

a = texto.endswith('.txt')
print(a)
b = texto.startswith('arq')
print(b)
c = texto.find('txt')
print(c)

data = '03/06/1999'
import re
r = True if re.match(r'\d+/\d+/\d+',data) else False
print(r)

r = True if re.match(r'\d+/\d+/\d+',texto) else False
print(r)

data_pattern = re.compile(r'\d+/\d+/\d+')
print(data_pattern)

r = True if data_pattern.match(data) else False
print(r)

texto = "blablabla 12/11/2020, kasfnf 10/10/1994"
nn = data_pattern.findall(texto)
print(nn)

p = re.compile(r'(\d+)/(\d+)/(\d+)$')
r = p.match('03/06/1999Rafael')
print(r)

r = p.match('03/06/1999')
print(r)

lista = [1,2,3]

for e in lista:
    print(e)
    
for e in reversed(lista):
    print(e)

class Complex:
    def __init__(self,r,i):
        self.r = r
        self.i = i
    def __repr__(self):
        return "({0}+{1}i)".format(self.r,self.i)
    def __add__(self, other):
        return Complex(self.r + other.r, self.i + other.i)

c1 = Complex(3,2)
print(c1)
c2 = Complex(2,4)
c3 = c1+c2
print(c3)

nome = "Rafael Manteiga Balbino"
nome2 = nome.replace("Rafael","Gabriel")
print(nome)
print(nome2)

import re

texto = "A data do meu aniversário é 03/06/1999"

print(texto)

padrao = re.compile(r"(\d+)/(\d+)/(\d+)")
texto2 = re.sub(padrao,r"\3-\2-\1",texto)
print(texto2)

voltando = re.compile(r"(\d+)-(\d+)-(\d+)")
textovolta = re.sub(voltando,r"\3/\2/\1",texto2)
print(textovolta)

import re

texto = "Java, java, Java"
print(texto)

texto = re.sub("java","Python",texto, flags=re.IGNORECASE)
print(texto)

texto = "Bora, irmão"
print(texto)

print(texto.strip("Bora,"))

texto = "Aprendendo Python"

print(texto.ljust(20))
print(texto.rjust(20))
print(texto.center(20))

print(format(texto,">20"))
print(format(texto,"<20"))
print(format(texto,"^20"))
print(format(texto,"->20s"))
y = 3.141592
print(format(y,">10"))

a = round(3.1415,2)
print(a)
a = round(3.7415,2)
print(a)

import numpy as np

l = [1,2,3]
print(l)
print(l*2)

x = np.array([1,2,3])
y = np.array([4,5,6])

print(x*2)
print(x+2)

print(np.sqrt(x))
print("\n")
matriz = np.matrix([])

matriz = np.matrix([[1,2],[3,4]])
print(matriz)
print("\n")
print(matriz.T)
print(matriz.I)

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
