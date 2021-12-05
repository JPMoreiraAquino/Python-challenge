
string = 'Flamengo Flamengo lost to Palmeira, in the Libertadores final.'

lista_1 = string.split(' ')
lista_2 = string.split(',')


for valor in lista_1:
    print(f"the word {valor} appear {lista_1.count(valor)}x in the sentence.")




