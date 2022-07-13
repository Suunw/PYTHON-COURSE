from datetime import date
atual = date.today().year
for pes in range (1, 8):
    nasc = int(input('Em que ano a pessoa nasceu? '))
    idade = atual - nasc
    if idade >= 21:
        print('Essa pessoa é maior: ')
    else:
        print('Essa pessoa é de menor:')