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

