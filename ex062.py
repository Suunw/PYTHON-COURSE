primeiro = int(input('Digite o primeiro termo da pa: '))
razao = int(input('Digite a razão da pa: '))
termo = primeiro
cont = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print('{} - '.format(termo), end='')
        termo += razao
        cont += 1
    print('PAUSA')
mais = int(input('Quantos termos tu quer mostrar a mais: '))