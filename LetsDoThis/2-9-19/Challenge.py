while True:
    try:
        friends = {"Jacob": "1234", "Tej": "4297", "Charlie": "238075"}
        if not friends:
            raise ValueError
    except ValueError as friends:
        print "Sorry I didn't understand that"

    friends.update({"Amogh":"56789"})
    print friends
    print "\n"

    user_input_name = raw_input("Please enter a name:\t")
    user_input_number = raw_input("Please enter a contact number:\t")

    friends.update({user_input_name: user_input_number})
    print friends

    answer = str(raw_input("Run again? (Yes/No): "))

    if answer.lower() == 'No'.lower():
        print 'Goodbye'
        break
    elif answer.lower() == 'Yes'.lower():
        print "Continuing Program :"
        continue
    else:
        print 'Goodbye!'
        break
