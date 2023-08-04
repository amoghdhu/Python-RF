while True:
    try:
        def calculate():
            operation = raw_input('''
    Please type in the math operation you would like to complete:
    + for addition
    - for subtraction
    * for multiplication
    / for division
    ''')


            number_1 = int(raw_input('Please enter the first number: '))
            number_2 = int(raw_input('Please enter the second number: '))

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
                print(number_1 / number_2)

            else:
                print('You have not typed a valid operator, please run the program again.')

            again()


        def again():
            calc_again = raw_input('''
        Do you want to calculate again?
        Please type YES or NO.
        ''')

            if calc_again.upper() == 'YES':
                calculate()
            elif calc_again.upper() == 'NO':
                print('See you later.')
            else:
                again()


        calculate()
    except:
        print "Please insert an appropriate value next time!"

        calc_again = raw_input('''
    Do you want to calculate again?
    Please type YES or NO.
        ''')

        if calc_again.upper() == 'YES':
            calculate()
        elif calc_again.upper() == 'NO':
            print('See you later.')
        else:
            again()




