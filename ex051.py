primeiro = int(input('Digite o primeiro termo da pa: '))
razao = int(input('Digite a razão da pa: '))
decimo = primeiro + (10 - 1) * razao
for c in range(primeiro, decimo, razao):
    print(c)