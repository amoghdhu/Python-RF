while True:
    try:
        month = str(raw_input('''
Please enter in a shortened form for a month:
Jan, Feb, Mar, Apr, May, June,
July, Aug, Sep, Oct, Nov, Dec
'''))
        if not month:
            raise ValueError
    except ValueError as month:
        print "Sorry I didnt understand that."

    if month.lower() == "Jan".lower():
        print "The month January is in the season winter.\n"""
    elif month.lower() == "Feb".lower():
        print "The month February is in the season winter.\n"""
    elif month.lower() == "Mar".lower():
        print "The month March is in the season spring.\n"""
    elif month.lower() == "Apr".lower():
        print "The month April is in the season spring.\n"""
    elif month.lower() == "May".lower():
        print "The month May is in the season spring.\n"""
    elif month.lower() == "June".lower:
        print "The month June is in the season summer.\n"""
    elif month.lower() == "July".lower():
        print "The month July is in the season summer.\n"""
    elif month.lower() == "Aug".lower():
        print "The month August is in the season summer.\n"""
    elif month.lower() == "Sep".lower():
        print "The month September is in the season fall.\n"""
    elif month.lower() == "Oct".lower():
        print "The month October is in the season fall.\n"""
    elif month.lower() == "Nov".lower():
        print "The month November is in the season fall.\n"""
    elif month.lower() == "Dec".lower():
        print "The month December is in the season winter.\n"""

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
