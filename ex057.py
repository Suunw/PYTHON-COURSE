sexo = str(input('Digite o seu sexo: [M/F] ')).strip().upper()[0]
while sexo not in 'MmFf':
        sexo = str(input('Dados invalidos, digite novamente o seu sexo [M/F] ')).strip().upper()[0]
print('Sexo {} registrado com sucesso!'.format(sexo))