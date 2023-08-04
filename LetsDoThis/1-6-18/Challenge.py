while True:
    try:
        sport = str(raw_input('''
Please pick a sport :
-Soccer
-Basketball
-Baseball
-Hockey
-Volleyball
-Football
'''))

        if not sport:
            raise ValueError
    except ValueError:
        print "Sorry I didn't understand that."
        break
    print "Lets make a {} team!".format(sport)
    player_count = 0
    print "Currently your player count is {}. ".format(player_count)
    nop = int(raw_input("Please enter the number of players you would like on your {} team. \n".format(sport)))
    if nop > 11:
        print "Sorry, you have exceeded the number of players on a team."
        break
    elif nop <= 1:
        print "Sorry, you are required to have a minimum of 2 players on your team."
        break
    print "You have {} players on your team!".format(nop)
    roster_string =   raw_input("Please enter {} different player names seperated by a comma : \n".format(nop))
    soccer_list = roster_string.split(", ")
    print "Here's your roster : \n"
    for name in soccer_list:
        print name
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
