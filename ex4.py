lista = []
maior = 0
menor = 0
for i in range(15):
    num = int(input('Digite um valor: '))
    lista.append(num)
    if i == 0:
        maior = menor = lista[i]
    else:
        if lista[i] > maior:
            maior = lista[i]
        if lista[i] < menor:
            menor = lista[i]
print('Lista =', lista)
print(f'O maior número da lista é {maior} na posição {lista.index(maior) + 1}')
print(f'O menor número da lista é {menor} na posição {lista.index(menor) + 1}')