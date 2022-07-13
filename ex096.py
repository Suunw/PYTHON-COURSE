def area(l, c):
    a = l * c
    print(f'A area de um terreno {l}x{c} é de: {a}m')


print('Controle de terrenos: ')
print('-'*30)
l = float(input('Largura em metros: '))
c = float(input('Comprimento em metros: '))
area(l, c)