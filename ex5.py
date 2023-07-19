fila = []
p = str(input('Quer adicionar ou remover? Digite fim para terminar o programa: ')).upper()
while p != 'ADICIONAR' and p != 'REMOVER' and p != 'FIM':
        print('Comando Invalido!')
        p = str(input('Quer adicionar ou remover? Digite fim para terminar o programa: ')).upper()
while p != 'FIM':
    if p == 'ADICIONAR':
        ad = str(input('Qual o nome do processo para ser adicionado? '))
        fila.append(ad)
        print(fila)
    elif p == 'REMOVER':
        if len(fila) == 0:
            print('Fila Vazia!')
        else:
            var = fila.pop()
            print(var)
            print(fila)
            len(fila)
    p = str(input('Quer adicionar ou remover? Digite fim para terminar o programa: ')).upper()