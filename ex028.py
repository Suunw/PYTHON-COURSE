import random
n1 = int(input('Digite e tente acertar um numero aleatorio de 0 a 5! '))
n = random.randint(0,5)
if n1 == n:
    print('Parabens, você acertou o numero {}'.format(n))
else:
    print('Que pena, você errou, o numero aleatorio foi: {} e você escolheu {}'.format(n, n1))