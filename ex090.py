aluno = dict()
aluno['nome'] = str(input('Nome do aluno: '))
aluno['media'] = float(input(f'Média de {aluno["nome"]}'))
if aluno['media'] >= 7:
    aluno['Situação'] = 'Aprovado'
elif 5 <= aluno['media'] < 7:
    aluno['Situação'] = 'Recuperação'
else:
    aluno['Situação'] = 'Reprovado'
    
for k, v in aluno.items():
    print(f'{k} é igual a {v}')