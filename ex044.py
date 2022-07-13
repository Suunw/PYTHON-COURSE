preço = float(input('Qual o preço do produto?'))
pagamento = int(input('''Escolha a opção de pagamento:
                         1 - A vista/Dinheiro
                         2 - A vista no cartão
                         3 - Em até 2x no cartão
                         4 - 3x ou mais no cartão'''))
if pagamento == 1:
    preçofinal = preço - (preço * 0.10)          
    print('Voce ganhou 10% de desconto e o preço final é:{}'.format(preçofinal))
elif pagamento == 2:
    preçofinal = preço - (preço * 0.05)
    print('Você ganhou 5% de desconto e o preço final é:{}'.format(preçofinal))
elif pagamento == 3:
    print('Infelizmente, não temos desconto para esta forma de pagamento, o preço final é:{}'.format(preço))
elif pagamento == 4:
    preçofinal = preço + (preço * 0.20)
    print('O preço final é:{}'.format(preçofinal))