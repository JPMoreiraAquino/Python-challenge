
string = 'O Flamengo Flamengo perdeu para o palmeira, na final da libertadores.'

lista_1 = string.split(' ')
lista_2 = string.split(',')


for valor in lista_1:
    print(f"A palavra {valor} apareceu {lista_1.count(valor)} x na frase.")




