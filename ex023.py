num = int(input('Informe um numero: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print("""Analizando o numero: {}:
      A unidade é: {}
      A dezena é: {}
      A centena é: {}
      O milhar é: {}""".format(num, u, d, c, m))


