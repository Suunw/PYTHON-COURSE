from tkinter import N


menu = 0
cont = 0
media = 0
soma = 0
maior = 0
menor = 0
while menu != '2':    
    num = int(input('Digite um numero: '))
    menu = str(input('Quer continuar? 1-SIM 2-NAO '))
    cont = cont + 1
    soma = soma + num
    media = soma / cont
    if maior == 0 or num >= maior: maior = num
    else: maior= maior
    if menor == 0 or num <= menor: menor = num
    else: menor= menor
print('A MEDIA É {:.4f}'.format(media))
print('O numero maior é {}'.format(maior))
print('O numero menor é: {}'.format(menor))