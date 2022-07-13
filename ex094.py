piazada = list()
pessoa = dict()
soma = media = 0
while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Nome: '))
    while True:
        pessoa['sexo'] = str(input('Sexo: [M/F]')).upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('Por favor digite apenas M ou F')
    pessoa['idade'] = int(input('Digite a idade: '))
    soma += pessoa['idade']
    piazada.append(pessoa.copy())
    while True:
        resp = str(input("Quer continuar?[S/N]")).upper()[0]
        if resp in 'SN':
            break
        print('Erro, apenas S ou N.')
    if resp == 'N': 
        break 
print('-='*30)
print(pessoa)
print(f'Ao todo temos {len(piazada)} pessoas cadastradas')
media = soma/len(piazada)
print(f'A media de idades é: {media:5.2f} anos ')
print(f'As mulheres cadastradas foram: ')
for p in piazada:
    if p['sexo'] in 'Ff':
        print(f'{p["nome"]} ',end='')
print('Lista das pessoa que estão acima da media: ')
for p in piazada:
    if p['idade'] >= media:
        print('     ')
        for k, v in p.items():
            print(f'{k} = {v}; ',end='')