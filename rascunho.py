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
