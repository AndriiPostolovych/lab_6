'''
Значення змінної x, що позначає деяку суму грошей в валюті p, замінити величиною
цієї ж суми в гривнях.
Постлович А.С. 122-В
'''
from enum import Enum
while True:
    while True:
        try:
            class converter(Enum):
                USD = 1
                EUR = 2
                CZK = 3
                PLN = 4
            x = float(input('amount of money: '))
            p = int(input('currency: '))
            if 1 <= p <= 4:
                if p == converter.USD.value:
                    print(x * 24.4)
                elif p == converter.EUR.value:
                    print(x * 26.6)
                elif p == converter.CZK.value:
                    print(x * 0.94)
                elif p == converter.PLN.value:
                    print(x * 6.26)
            else:
                print('Invalid data')
                break
            break
        except ValueError:
            print('Input correctly data: ')
    key = input('Again? Yes - 1, no - 2: ')
    if key == '1':
        continue
    else:
        print('Bye')
        break