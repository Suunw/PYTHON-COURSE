from numpy import true_divide


print('-----CAIXA ELETRONICO-----')
valor = int(input('Qual valor tu queres sacar? '))
total = valor
ced = 50
totced = 0
while True:
    if total >= ced:
        total -= ced
        totced += 1
    else:
        print(f'total de {totced} cedulas de {ced} Reais')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10 
        elif ced == 10:
            ced = 1
        totced = 0
        if total == 0:
            break