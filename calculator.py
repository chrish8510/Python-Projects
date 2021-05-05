def welcome():
    print("Welcome to Calculator!")
# Make sure to call the function
welcome()

# Define our function
def calculate():
    # User enters any numbers for input
    number_1 = int(input('Please enter the first number: '))
    number_2 = int(input('Please enter the second number: '))
    # operation for calculations
    operation = input('''
Please type in the math operation you would like to complete:
+ for addition
- for subtraction
* for multiplication
/ for division
''')

    if operation == '+':
        print('{} + {} = '.format(number_1, number_2))
        print(number_1 + number_2)

    elif operation == '-':
        print('{} - {} = '.format(number_1, number_2))
        print(number_1 - number_2)

    elif operation == '*':
        print('{} * {} = '.format(number_1, number_2))
        print(number_1 * number_2)

    elif operation == '/':
        print('{} / {} = '.format(number_1, number_2))
        # below is for ZeroDivisionError
        if number_2 == 0:
            print("Divide by 0 Error")
        else:
            print(number_1, '/', number_2, '=', number_1 / number_2)

    else:
        print('You have not typed a valid operator, please run the program again.')

# Add again() function to calculate() function
    again()


# Define again() function to ask user if they want to use calculator again
def again():
    calc_again = input('''
    Do you want to calculate again? 
    Please type Y for yes and Y for no.
    ''')
    # Accept 'y' or 'Y' by adding str.upper()
    # If user types Y, run the calculate() function
    if calc_again.upper() == 'Y':
        calculate()
    # Accept 'n' or 'N' by adding str.upper()
    # If user types N, say good-bye to the user and end the program
    elif calc_again.upper() == 'N':
        print('See you later.')

    # If user types another key, run the function again
    else:
        again()


# Call calculate() outside of the function
calculate()