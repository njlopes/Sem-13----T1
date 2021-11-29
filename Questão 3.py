invert=[]
n=int(input())
for i in range(n):
      numero=float(input())
      invert.insert(0, numero)
print(invert)

listanota=[]
qnt=0
soma=0
for i in range(n):
    valor=float(input())
    soma+=valor
    qnt+=1
    listanota.append(valor)
print(listanota)
if n==0:
      print('SEM NOTAS')
else:
      media=soma/qnt
      print(f'{media:.1f}')

listavogal=[]
listaconso=[]
qnt=0
for i in range(n):
    vogal=input()[0]
    if vogal in 'bcçdfghjklmnpqrstvwxyzBCÇDFGHJKLMNPQRSTVWXYZ':
          listaconso.append(vogal)
    if vogal in 'aeiouAEIOU':
          qnt+=1
print(qnt)
print(listaconso)
