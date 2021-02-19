leapYear = input('Enter Current Year: ')
year_num = int(leapYear)

if year_num % 4 == 0:
    print('Year', year_num,  'is a leap year.')
else:
    print('Year', year_num, 'is not a leap year.')
