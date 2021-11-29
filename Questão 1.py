listanumeros= []

for i in range(10):
    listanumeros.append(int(input()))

def somalista(lista):
    totalSoma = 0
    for numerolista in lista:
        totalSoma += numerolista
    return totalSoma

def produtolista(lista):
    totalProduto = 1
    for numerolista in lista:
        totalProduto *= numerolista
    return totalProduto

print(listanumeros)
print(somalista(listanumeros))
print(produtolista(listanumeros))
