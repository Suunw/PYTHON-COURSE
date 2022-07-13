soma = 0
nome = str(input('Qual o nome do jogador: '))
partidas = int(input("Quantas partidas ele jogou? "))
for i in range(0, partidas):
    gol=int(input(f'Quantos gols na partida {i+1}: '))
    soma += gol
print(f'O jogador acertou {soma} gols')