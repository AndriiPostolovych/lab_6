'''
За s-назвою місяця визначити відповідну пору року.
Постлович А.С. 122-В
'''
from enum import Enum
while True:
    while True:
        try:
            class month (Enum):
                January = 1
                February = 2
                March = 3
                April = 4
                May = 5
                June = 6
                July = 7
                August = 8
                September = 9
                October = 10
                November = 11
                December = 12
            class season (Enum):
                Winter = 1
                Spring = 2
                Summer = 3
                Autumn = 4
            s = int(input('month: '))
            if 1 <= s <= 12:
                if s == month.March.value or s == month.April.value or \
                    s == month.May.value:
                    print(season.Spring)
                elif s == month.June.value or s == month.July.value or \
                    s == month.August.value:
                    print(season.Summer)
                elif s == month.September or s == month.October.value or \
                    s == month.November.value:
                    print(season.Autumn)
                elif s == month.December.value or s == month.January.value or \
                    s == month.February.value:
                    print(season.Winter)
            else:
                print('Incorect data')
                break
            break
        except ValueError:
            print('Input correctly data')
    key = input('Again? Yes - 1, no - 2: ')
    if key == '1':
        continue
    else:
        print('Bye')
        break