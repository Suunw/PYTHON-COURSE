num = (int(input('Digite um numero: ')),
       int(input('Digite mais um numero: ')),
       int(input('Digite mais um numero: ')),
       int(input('Digite mais um numero: '))),
print(f'Você digitou os valores: {num}')
print(f'O numero 9 apareceu: {num.count(9)}')
if 3 in num:
    print(f'O valor 3 apareceu na {num.index(3)+1}')
else:
    print('O valor 3 não foi digitado.')
for n in num:
    if num % 2 == 0:
        print(num)
