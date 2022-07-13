from random import randint
from time import sleep

def sorteia(lista):
    x = 1
    while True:
        valores.append(randint(1,10))  
        x += 1
        if x == 6:
            break
    print(f'Sorteando 5 números da lista...',end=' ')
    for c in valores:
        print(c,end=' ', flush=True)
        sleep(1)
    
        

def soma(pares):
    s = 0
    c = 1
    for v in valores:
        if v % 2 == 0:
            s += v
        if v % 2 == 0:
            npar.append(v)
        if  c == len(valores):
            break
        c += 1
    print()
    print(f'Somando os valores pares {npar} , O resultado foi {s}')


valores = []
npar = []
sorteia(valores)
soma(valores)
