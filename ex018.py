import math
angulo = int(input('Digite um angulo qualquer para calcular o seno, cosseno e tangente: '))
s = math.sin(math.radians(angulo))
c = math.cos(math.radians(angulo))
t = math.tan(math.radians(angulo))
print('O seno do angulo é: {:.2f}, o cosseno é: {:.2f}, e a tangente é: {:.2f}'.format(s, c, t))