import imp
from tkinter import N


numeros = list()
par = list()
impar = list()
while True:
    n = int(input('Digite um valor qualquer: '))
    numeros.append(n)
    if n % 2 == 0:
        par.append(n)
    elif n % 2 == 1:
        impar.append(n)
    r = str(input('Quer continuar? [Y/N]'))
    if r in 'Nn':
        break
print(F'A lista é: {numeros}')
print(f'A lista com os numeros pares é: {par}')
print(f'A lista com os numeros impares é: {impar}')
