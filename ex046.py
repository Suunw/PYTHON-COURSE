from time import sleep
print('\033[1;92mContagem regressiva de fogos de artificio!\33[m')
i = int(input('''Quer começar?
              1 - SIM
              2 - NÃO '''))
if i == 1:
    for c in range(10, 0, -1):
        sleep(1)
        print(c)
    print('\033[1;33mBOOM BOOM PA PA PA PA\33[m')