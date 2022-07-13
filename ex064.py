num = soma = cont = 0
while num != 999:
    num = int(input('Digite um numero, [999] para sair: '))
    soma = soma + num
    cont = cont + 1
print('A soma entre os numeros é: {} e você digitou {} numeros'.format(soma - 999, cont - 1))