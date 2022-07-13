soma = 0
for c in range(1, 501):
    if c % 2 != 0 and c % 3 == 0:
        soma += c
print('A Soma de todos o numeros divisiveis por 3 de 1 a 500 é:{}'.format(soma))