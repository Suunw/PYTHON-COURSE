a1 = float(input('Enter the value of a random line: '))
a2 = float(input('Enter another value: '))
a3 = float(input('Enter another value: '))
if a1 + a2 > a3 and a2 + a3 > a1 and a1 + a3 > a2:
    print('You can make a triangle!')
    if a1 == a2 == a3:
         print('Triangulo equilatero!')
    if a1 != a2 != a3:
        print('Triangulo escaleno!')
    else: 
        print('Isosceles')
else:
    print('You cant')