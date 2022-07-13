import random
lista = []
for i in range(0, 5):
    n = random.randint(1, 9)
    lista.append(n)
print(lista)
print(f'O maior valor dentro da lista foi {max(lista)}')
print(f'O menor valor dentro da lista foi {min(lista)}')