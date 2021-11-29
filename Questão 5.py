lista1 = []
lista2 = []
listaInter = []

for i in range(25):
    lista1.append(int(input()))

for j in range(25):
    lista2.append(int(input()))

for m in range(25):
    listaInter.append(lista1[m])
    listaInter.append(lista2[m])

print(lista1)
print(lista2)
print(listaInter)
