string = 'Flamengo Flamengo lost to Palmeira, in the Libertadores final.'

lista_1 = string.split(' ')
lista_2 = string.split(',')

word = ''

contagem = 0

for valor in lista_2:
    qtd_vezes = lista_2.count(valor)

    if qtd_vezes > contagem:
        contagem = qtd_vezes
        palavra = valor
print(f"the word that appears more iften is {word} ({contagem}x)")