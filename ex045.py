from random import randint
print('\033[1;92mVamos jogar jokenpo!\33[m')
print('''Regras:Pedra ganha da tesoura, Tesoura ganha do papel
        Papel ganha da pedra.
      Opções: \033[1;31m1 - Pedra\33[m
              \033[1;31m2 - Papel\33[m
              \033[1;31m3 - Tesoura\33[m''')
escolha = int(input('Escolha a sua jogada:'))
computador = randint(1, 3)
if escolha == 1 and computador == 1:
    print('\033[1;33mEMPATE!\33[m, o computador jogou {}, PEDRA'.format(computador))
elif escolha == 1 and computador == 2:
    print('\033[1;31mVOCÊ PERDEU\33[m, o computar jogou {}, PAPEL.'.format(computador))
elif escolha == 1 and computador == 3:
    print('\033[1;92mVOCÊ GANHOU!\33[m, o computador jogou {}, TESOURA.'.format(computador))
elif escolha == 2 and computador == 1:
    print('\033[1;92mVOCÊ GANHOU!\33[m, o computador jogou {}, PEDRA.'.format(computador))
elif escolha == 2 and computador == 2:
    print('\033[1;33mEMPATE!\33[m, o computador jogou {}, PAPEL.'.format(computador))
elif escolha == 2 and computador == 3:
    print('\033[1;31mVOCÊ PERDEU\33[m, o computador jogou {}, TESOURA.'.format(computador))
elif escolha == 3 and computador == 1:
    print('\033[1;31mVOCÊ PERDEU\33[m, o computador jogou {}, PEDRA'.format(computador))
elif escolha == 3 and computador == 2:
    print('\033[1;92mVOCÊ GANHOU!\33[m, o computador jogou {}, PAPEL.'.format(computador))
elif escolha == 3 and computador == 3:
    print('\033[1;33mEMPATE!\33[m, o computador jogou {}, TESOURA'.format(computador))