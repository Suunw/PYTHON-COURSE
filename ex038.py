n1 = int(input('Digite um numero inteiro: '))
n2 = int(input('Digite um outro numero inteiro: '))
if n1 > n2:
    print('O valor maior é {}'.format(n1))
elif n2 > n1:
    print('O valor Maior é {}'.format(n2))
else:
    print('Os dois numeros são iguais ')