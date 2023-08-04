while True:
    from datetime import *

    today = date.today()
    print("Today: " + today.strftime('%A %d, %b %Y'))

    question = input("What is your Date of Birth? dd/mm/yyyy")
    variable = question.split("/")
    Day = int(variable[0])
    Month = int(variable[1])
    Year = int(variable[2])
    var = date(Year, Month, Day)

    numberOfDays = (today - var).days

    age = numberOfDays // 365
    print("You are " + str(age) + " years old.")

    day = var.strftime("%A")
    print("You were born on a " + day + ".")

    print("You have spent " + str(numberOfDays) + " days on Earth.")

    thisYear = today.year

    nextBirthday = date(thisYear, Month, Day)
    if today < nextBirthday:
      gap = (nextBirthday - today).days
      print("Your birthday is in " + str(gap) + " days.")
    elif  today == nextBirthday:
      print("Today is your birthday! Happy Birthday!")
    else:
      nextBirthday = date(thisYear+1, Month, Day)
      gap = (nextBirthday - today).days
      print("Your birthday is in " + str(gap) + " days.")
    answer = input("Run again? (Yes/No): ")

    if answer.lower() == 'No'.lower():
        print
        'Goodbye'
        break
    elif answer.lower() == 'Yes'.lower():
        print
        "Continuing Program :"
        continue
    else:
        print
        'Goodbye!'
        break
