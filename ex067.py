print("Calculador de tabuada!! ")
while True:
    num = int(input('Digite um numero:'))
    if num < 0:
        break
    for c in range (1, 11):
        print(f'{num} x {c} = {num*c}')
print('PROGRAMA ENCERRADO!')
       
           