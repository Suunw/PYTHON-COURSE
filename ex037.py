n = int(input('Digite um numero inteiro aleatorio: '))
n1 = int(input('''Voce quer converter o numero para:
               1 - Binario
               2 - Octal
               3 - Hexadecimal
               Escolha uma opção:'''))
bi = bin(n)
oc = oct(n)
he = hex(n)
if n1 == 1:
    print('O seu numero {} convertido para Binario é:{}!'.format(n, bi[2:]))
elif n1 == 2:
    print('O seu numero {} convertido para Octal é:{}!'.format(n, oc[2:]))
elif n1 == 3:
    print('O seu numero {} convertido para Hexadecimal é:{}!'.format(n, he[2:]))
else:
    print('Opção invalida, tente novamente.')