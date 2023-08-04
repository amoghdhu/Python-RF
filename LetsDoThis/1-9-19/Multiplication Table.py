while True:
    num = int(input("Which number would you like a multiplication table of?\n"))

    for i in range(1, 11):
        print (num, 'x', i, '=', num * i)
    answer = str(input("Run again? (Yes/No): \t"))

    if answer == 'No'.lower():
        print ('Goodbye')
        break
    elif answer == 'Yes'.lower():
        print ("Continuing Program :")
        continue
    else:
        print ('Goodbye! Not valid option.')
        break


