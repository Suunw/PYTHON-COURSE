from subprocess import list2cmdline


lista = list()
mai = 0
men = 0
for c in range(0,5):
    lista.append(int(input('Digite um valor')))
    if c == 0:
        mai = men = lista[c]
    else:
        if lista[c] > mai:
            mai = lista[c]
        if lista[c] < men:
            men = lista[c]
print(f'a sua lista é {lista}')
print(f'O menor valor digitado foi {men}, e o maior {mai}')
