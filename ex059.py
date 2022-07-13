valor1=int(input('Digite o primeiro valor: '))
valor2=int(input('Digite o segundo valor: '))
menu = 0
while (menu != 5):
    menu=int(input('''======MENU=====
    [1] SOMAR
    [2] MULTIPLICAR
    [3] MAIOR
    [4] NOVOS NUMEROS
    [5] SAIR DO PROGRAMA\n'''))
    if menu == 1:
        print('A soma dos dois valores é: {}'.format(valor1 + valor2))
    elif menu == 2:
        print('A multiplicação dos dois valores é: {}'.format(valor1 * valor2))
    elif menu == 3:
        if valor1 > valor2:
            print('O maior valor entre os dois valores é: {}'.format(valor1))
        else:
            print('O maior valor entre os dois valores é: {}'.format(valor2))
    elif menu == 4:
        valor1=int(input('Digite o primeiro valor: '))
        valor2=int(input('Digite o segundo valor: '))
    elif menu == 5:
        print('Programa finalizado com sucesso!')
print('Fim')