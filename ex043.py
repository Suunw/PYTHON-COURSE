altura = float(input('Digite a sua altura: '))
peso = float(input('Digite o seu peso: '))
imc = peso / (altura ** 2) 
if imc < 18.5:
    print('Voce esta abixo do peso normal')
elif 18.5 <= imc < 25:
    print('Parabens, voce esta na feixa de peso normal')
elif 25 <= imc < 30:
    print('Voce esta sobrepeso')
elif 30 <= imc < 40:
    print('Voce esta em obsidade, cuidado')
elif imc >= 40:
    print('Voce esta em obisiade mormiba, cuidado!')