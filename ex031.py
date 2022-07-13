d = int(input('Enter the distance of your trip: '))
if d <= 200:
    print('The price of your trip is: {}'.format(d * 0.50))
else:
    print('The price of your trip is: {}'.format(d * 0.45))