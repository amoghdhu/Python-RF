while True:
    try:
        age = int(raw_input('''Please enter your age: '''))
    except ValueError:
        print "Sorry I didn't understand that."
        continue
    else:
        break
if age >= 18:
    print "You are allowed to watch the movie!"
else:
    print "You are not old allowed to watch the movie."
    print "Please come back in {} years".format(18 - age)




