numeros = list()
while True:
    n = int(input('Digite um numero: '))
    numeros.append(n)
    r = str(input("Quer continuar? [Y/N]"))
    if r in 'Nn':
        break
if 5 in numeros:
    print('Tem um numero cinco na lista!')
else:
    print('Não tem nenhum numero cinco na lista.')

print(F'A lista tem {len(numeros)} numeros! ')
numeros.sort(reverse=True)
print(numeros)