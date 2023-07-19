livros = []
for i in range(4):
    livros.append(input('Digite o nome dos livros: '))
livro_favorito = str(input('Informe seu livro favorito: '))
for l in range(len(livros), 0, -1):
    var = livros.pop()
    livros.append(var)
    if var == livro_favorito:
        livros.remove(livro_favorito)
    var = livros.pop(0)
    livros.append(var)
print('Livros', livros)