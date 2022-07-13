a = float(input('Enter a random number: '))
b = float(input('Enter another random number: '))
c = float(input('Enter another random number: '))
biggest = a
if (b > biggest):
    biggest = b
if (c > biggest):
    biggest = c
print('The biggest number is: {}!'.format(biggest))