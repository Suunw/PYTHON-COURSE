vel = int(input('Qual a velocidade do seu carro? '))
if vel > 80:
    vel1 = vel - 80
    preco= vel1 * 7
    print('Ah, que pena, o seu carro foi multado, a sua velocidade é de {}km/h, e você pagara uma multa de R$:{}'.format(vel, preco))
else:
    print('Muito bem, a sua velocidade é de {}, continue andando nos limites!'.format(vel))
