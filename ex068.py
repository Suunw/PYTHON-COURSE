from random import randint
v = 0
while True:
    jogador = int(input('Jogue um numero!'))
    computador = randint(0, 11)
    total = jogador + computador
    escolha = int(input('Par ou impar? 1- Par 2- Impar'))
    if escolha == 1:
        if total % 2 == 0:
            print('Você ganhou!')
            v += 1
        else:
            print('Você perdeu')
    elif escolha == 2:
        if total % 2 == 1:
            print('Você venceu!')
            v +=1
        else:
            print('Você perdeu')
    print('Vamos jogar novamente!')
print(f'Você venceu {v}')