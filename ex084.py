
temp = []
pric = []

while True:
    temp.append(str(input('Nome: ')))
    temp.append(float(input('Peso: ')))
    if len(pric) == 0:
        mai = men = temp[1]
    else:
        if temp[1] > mai:
            mai = temp[1]
        if temp[1] < men:
            men = temp[1]
    pric.append(temp[:])
    temp.clear()
    resp = str(input('Quer continuar? [S/N]'))
    if resp in 'Nn':
        break
print(f"Os dados foram: {pric}")
print(f'Ao todo você cadastrou: {len(pric)} pessoas')
print(f'O maior peso foi de {mai} kg')
for p in pric:
    if p[1] == mai:
        print(f'{p[0]}')
print(f'O menor peso foi de {men} kg')
for p in pric:
    if p[1] == men:
        print(f'{p[0]}')
print()