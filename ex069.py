from ast import If


cid = homens = mulheres20 = 0
while True:
    sexo = str(input('Qual o seu sexo? [M/F]')).strip().upper()
    idade = int(input('Qual a sua idade? '))
    if idade > 18: 
        cid += 1
    if sexo == 'M':
        homens += 1
    if sexo == 'F' and idade < 20:
        mulheres20 += 1
    parar = int(input('Digite 1 para parar, e 2 para continuar: '))
    if parar == 1:
        break
print(f'O numero de pessoas com mais de 18 anos é {cid}, o numero de homens é {homens} e o numero de mulheres mais jovens de 20 anos é {mulheres20}')