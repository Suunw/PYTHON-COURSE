nota1 = float(input('Digite a sua primeira nota: '))
nota2 = float(input('Digite a sua segunda nota: '))
media = (nota1 + nota2) / 2
if 7 > media >= 5:
    print('Sua media é de: {} e você esta em recuperação'.format(media))
elif media < 5:
    print('O aluno esta reprovado')
elif media >= 7:
    print('O aluno esta aprovado!')