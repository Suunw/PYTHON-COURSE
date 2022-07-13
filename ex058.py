import random
n1 = int(input('Digite e tente acertar um numero aleatorio de 0 a 10! '))
n = random.randint(0,10)
palpites = 0
while n1 != n:
    n1 = int(input('Numero errado, tente acertar novamente: '))
    palpites += 1
print('Parabens, você acertou o numero {}, com {} tentativas'.format(n, palpites + 1))

