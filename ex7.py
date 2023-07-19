palavra = str(input('Imforme uma palavra com mais de 4 caracteres: '))
while len(palavra) < 4:
    print('A palavra não atingiu o tamanho mínimo necessário!')
    palavra = str(input('Informe uma palavra com mais de 4 caracteres: '))
a = ''
for i in palavra[:: -1]:
    a += i
b = ''
meta = int(len(palavra) / 2)
for i in palavra[0:meta:1]:
    b += i
c = ''
for i in palavra[meta:len(palavra):1]:
    c += i
d = ''
meta_final = ''
meta_comeco = ''
for i in palavra[meta:len(palavra):1]:
    meta_final += i
for i in palavra[0:meta:1]:
    meta_comeco += i
d = meta_final + meta_comeco
e = ''
vogal = ''
cons = ''
for i in palavra:
    if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u':
        vogal += i
    else:
        cons += i
e = vogal + cons
f = ''
meta = int(len(palavra) / 2)
meta_final = []
meta_comeco = []
for i in palavra[0:meta:1]:
    meta_comeco.append(i)
for i in palavra[meta:len(palavra):1]:
    meta_final.append(i)
while len(meta_final) > 0:
    if len(meta_comeco) > 0:
        letra1 = meta_comeco[0]
        meta_comeco.pop(0)
        f += letra1
    meta2 = meta_final[0]
    meta_final.pop(0)
    f += meta2
print(f'Letra A = A string de tras para frente é: {a}')
print(f'Letra B = A primeira metade da string é: {b}')
print(f'Letra C = A segunda metade da string é: {c}')
print(f'Letra D = A string com a segunda metade antes da primeira metade: {d}')
print(f'Letra E = A string com todas as vogais antes de todas as consoantes: {e}')
print(f'Letra F = A string com as letras intercaladas: {f}')