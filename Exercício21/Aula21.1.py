string = 'O Flamengo Flamengo perdeu para o palmeira, na final da libertadores.'

lista_1 = string.split(' ')
lista_2 = string.split(',')

palavra = ''

contagem = 0

for valor in lista_2:
    qtd_vezes = lista_2.count(valor)

    if qtd_vezes > contagem:
        contagem = qtd_vezes
        palavra = valor
print(f"A palavra que apareceu mais vezes é {palavra} ({contagem}x)")