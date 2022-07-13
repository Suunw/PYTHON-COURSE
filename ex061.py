primeiro = int(input('Digite o primeiro termo da pa: '))
razao = int(input('Digite a razão da pa: '))
termo = primeiro
cont = 1
while cont <= 10:
    print('{} - '.format(termo), end='')
    termo += razao
    cont += 1
print('FIM')
