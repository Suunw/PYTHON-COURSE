name = str(input('Write your name here: ')).strip()
print('Your name is uppercase letters is: {}, and in lowercase letters is: {}'.format(name.upper(),name.lower()))
print('Your name has {} letters!'.format(len(name) - name.count(' ')))
divided = name.split()
print('Your first name is: {}, and it has {} letters!'.format(divided[0], len(divided[0])))