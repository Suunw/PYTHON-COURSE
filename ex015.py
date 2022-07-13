dias = int(input('Por quantos dias o carro foi alugado? '))
km = int(input('Quantos km foram rodados? '))
pf: float = dias * 60 + km * 0.15
print('O preço final é de:R${} Reais'.format(pf))