l = float(input('Bem vindo ao calculador de litros de tinta, digite a largura da sua parede: '))
al = float(input('E agora, a altura: '))
ar: float = l * al
m: float = ar / 2
print('A sua parede tem {} metros quadrados, e utilizara {} litros de tinta!'.format(ar, m))