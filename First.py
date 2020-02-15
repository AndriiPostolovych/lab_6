'''
За датою d, m, y визначити дату наступного і попереднього дня. В програмі врахувати
наявність високосних років.
Постлович А.С. 122-В
'''
while True:
    while True:
        try:
            days = range (1, 32)
            mounths = range (1, 13)
            years = range (1901, 2020)
            d, m, y = int (input ( 'day: ')), \
                      int (input ( 'mounth: ')), \
                      int (input ( 'year: '))
            if (m == 1 or m == 3 or m == 5 or m == 7 or \
                    m == 8 or m == 10 or m == 12) and 1 < d <= 30\
                    and 1901 <= y <= 2019:
                print('Previous date -',d-1,'.',m,'.',y)
                print('Next date -',d+1,'.',m,'.',y)
            elif (m == 4 or m == 6 or m == 9 or m == 11)\
                    and 1 < d <= 29 \
                    and 1901 <= y <= 2019:
                print('Previous date -',d-1,'.',m,'.',y)
                print('Next date -',d+1,'.',m,'.',y)
            elif m == 2 and 1 < d <= 27 and y%4 != 0 \
                    and 1901 <= y <= 2019:
                print('Previous date -',d-1,'.',m,'.',y)
                print('Next date -',d+1,'.',m,'.',y)
            elif m == 2 and 1 < d <= 28 and y%4 == 0 \
                    and 1901 <= y <= 2019:
                print('Previous date -',d-1,'.',m,'.',y)
                print('Next date -',d+1,'.',m,'.',y)
            elif (m == 1 or m == 3 or m == 5 or m == 7 or \
                    m == 8 or m == 10) and d == 31\
                    and 1901 <= y <= 2019:
                print('Previous date -',d-1,'.',m,'.',y)
                print('Next date -',1,'.',m+1,'.',y)
            elif (m == 4 or m == 6 or m == 9 or m == 11) \
                    and d == 30 \
                    and 1901 <= y <= 2019 and y % 4 != 0:
                print('Previous date -', d-1,'.',m,'.', y)
                print('Next date -',1,'.',m+1,'.', y)
            elif m == 2 and d == 29 and y%4 == 0 \
                    and 1901 <= y <= 2019:
                print('Previous date -',d-1,'.',m,'.',y)
                print('Next date -',1,'.',m+1,'.',y)
            elif m == 2 and d == 28 and y%4 != 0 \
                    and 1901 <= y <= 2019:
                print('Previous date -',d-1,'.',m,'.',y)
                print('Next date -',1,'.',m+1,'.',y)
            elif (m == 5 or m == 7 or m == 8 or m == 10 or m == 12) and d == 1 \
                    and 1901 <= y <= 2019:
                print('Previous date -',30,'.',m-1,'.',y)
                print('Next date -',d+1,'.',m,'.',y)
            elif (m == 4 or m == 6 or m == 9 or m == 11)\
                and d == 1 and 1901 <= y <= 2019 and y%4 != 0:
                print('Previous date -',31,'.',m-1,'.',y)
                print('Next date -',d+1,'.',m,'.',y)
            elif m == 3 and d == 1 and 1901 <= y <= 2019:
                print('Previous date -',28,'.',m-1,'.',y)
                print('Next date -',d+1,'.',m,'.',y)
            elif m == 3 and d == 1 and 1901 <= y <= 201:
                print('Previous date -',29,'.',m-1,'.',y)
                print('Next date -',d+1,'.',m,'.',y)
            elif m == 1 and d == 1 and 1901 <= y <= 2019:
                print('Previous date -',31,'.',12,'.',y-1)
                print('Next date -',d+1,'.',m,'.',y)
            elif m == 12 and d == 31 and 1901 <= y <= 2019:
                print('Previous date -',d-1,'.',m,'.',y)
                print('Next date -',1,'.',1,'.',y+1)
            break
        except ValueError:
            print('Input correctly data')
    key = input('Again? Yes - 1, no - 2: ')
    if key == '1':
        continue
    else:
        print('Bye')
        break