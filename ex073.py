from os import times


time = ('Palmeiras', 'Corinthians', 'Atletico-pr', 'Atletico Mineiro', 'Internacional', 'Fluminense', 'Bota Fogo', 'Santos',
        'São paulo', 'Bragantino', 'Avai', 'Atletico Goianiense', 'Ceara', 'Flamengo', 'Coritiba', 'America FC', 'Goias', 'Cuiaba', 'Fortaleza', 'Juventude')
print(f'Os primeiros cinco colocados do brasileirão são: {time[:5]}')
print(f'Os ultimos quatro colocados da tabela são: {time[16:20]}')
print(f'A ordem alfabetica dos times é: {sorted(time)}')
print(f'O time Coritiba esta na posição: {time.index("Coritiba")+1} posição')
