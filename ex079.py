numeros = list()
while True:
    n = int(input('Digite um numero: '))
    if n not in numeros:
        numeros.append(n)
        print('Valor adicionado com sucesso!')
    else:
        print('Valor Duplicado, não é possivel adicionar.')


    r = str(input('Quer continuar? [S/N]'))
    if r in 'Nn':
        break
numeros.sort()
print(f'A sua lista em ordem crescente é: {numeros}')