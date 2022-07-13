s = float(input('Enter your wage: '))
if s > 1250:
    print('Your new wage is: {}'.format(s * 0.10 + s))
else:
    print('Your new wage is {}'.format(s * 0.15 + s))
