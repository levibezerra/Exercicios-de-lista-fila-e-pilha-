lista = []
for i in range(1, 11):
    lista.append(int(input('Digite um número: ')))
print(lista)
var = lista.pop(0)
var = lista.append(var)
print(lista)