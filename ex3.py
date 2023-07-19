lista = []
pares = []
impares = []
for i in range(20):
    num = int(input('Digite 20 números inteiros: '))
    while num < 0:
        print('Esse número não é inteiro!')
        num = int(input('Digite 20 números!'))
    lista.append(num)
for i in lista:
    if i % 2 == 0:
        pares.append(i)
    else:
        impares.append(i)
print('Lista =', lista)
print('Pares =', pares)
print('Impares=', impares)