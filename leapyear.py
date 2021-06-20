# user input for the year
leapYear = input('Enter Current Year: ')
# name the variable input to year_num
year_num = int(leapYear)
# leap year happens once every 4 years. if function is for the leap year, and else function is for other than leap year.
if year_num % 4 == 0:
    print('Year', year_num,  'is a leap year.')
else:
    print('Year', year_num, 'is not a leap year.')
