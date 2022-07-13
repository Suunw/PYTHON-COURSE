import math

ca = float(input('Digite o valor do cateto adjascente do triangulo: '))
co = float(input('Digite o valor do cateto oposto do triangulo '))
ra =math.hypot(co, ca)

print('A hipotenusa do seu triangulo é {:.2f}'.format(ra))
