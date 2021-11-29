lista=[]
n=int(input())
for i in range(n):
    lista.append(n)
    lista.insert(n, 0)
    lista.remove(n)
print(lista)

lista2=[]
for i in range(1, n+1):
    lista2.append(i)
print(lista2)

lista3=[]
for i in range(1, n+1):
    lista3.append(int(input()))
print(lista3)

lista4=[]
for i in range(1, n+1):
    lista4.append(int(input()))
print(lista4[::-1])
