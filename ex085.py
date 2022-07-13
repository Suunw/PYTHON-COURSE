lista = [], []
print(f'Informe sete numeros!')
for i in range(0,7):
    n = int(input(f'Digite o {i+1} numero: '))
    if n % 2 == 0:
        #par
        lista[0].append(n)
    else:
        lista[1].append(n)
lista[0].sort
lista[1].sort
print(f'Os numeros pares são: {lista[0]}')
print(f'Os numeros impares são: {lista[1]}')