preço = int(input('Digite o valor da casa que você vai comprar:'))
tempo = int(input('Em quantos anos? '))
salario = int(input('Qual o seu salario?'))
prestação = preço / (tempo * 12) 
minimo = salario * 30 / 100
if prestação <= minimo:
    print('Emprestimo pode ser concedido!')
else:
    print('Emprestimo negado.')