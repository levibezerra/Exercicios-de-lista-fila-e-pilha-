lista1 = []
lista2 = []
lista3 = []
for i in range(5):
    num = int(input('Digite um número inteiro: '))
    lista1.append(num)
print('Lista1 = ', lista1)
for i in range(5):
    num = int(input('Digite um número: '))
    lista2.append(num)
print('Lista2', lista2)
for i in lista1:
    for l in lista2:
        if(l == i):
            lista3.append(l)
print('O conjunto interceção lista1 e lista2 =', lista3)