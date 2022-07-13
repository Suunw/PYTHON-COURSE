n = int(input('Digite um numero para verificar se é primo ou não: '))
tot = 0
for c in range(1, n + 1):
    if n % c == 0:
        print('\033[34m', end=' ')
        tot += 1
    else:
        print('\033[31m', end=' ')
    print('{}'.format(c), end=' ')
print('O numero {} foi divisivel {} vezes!'.format(n, tot))