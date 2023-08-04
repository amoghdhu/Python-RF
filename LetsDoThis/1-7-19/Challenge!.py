from random import choice
while True:
    print ("""
Welcome to Rock, Paper, Scissors. The game 
is simple. You are playing the cpu and have 
3 options: Rock, Paper, Scissors.
-Rock beats paper, loses to scissors.
-Paper beats scissors, loses to rock.
-Scissors beats rock, loses to paper.
Good luck!\n """)

    user = raw_input("""
Please select an option :
Rock
Paper 
Scissors\n
""")

    computer = choice(["Rock", "Paper", "Scissors"])

    if user.lower() == "Rock".lower() or user == "1" and computer == "Rock".lower():
        print "Computer chose rock : Tie"
    elif user.lower() == "Rock".lower() or user == "1" and computer == "Paper".lower():
        print "Computer chose paper : You lost, nice try!"
    elif user.lower() == "Rock".lower() or user == "1" and computer == "Scissors".lower():
        print "Computer chose scissors : You won, great job!"

    elif user.lower() == "Paper".lower() or user == "2" and computer == "Rock".lower():
        print "Computer chose rock : You won, great job!"
    elif user.lower() == "Paper".lower() or user == "2" and computer == "Paper".lower():
        print "Computer chose paper : Tie"
    elif user.lower() == "Paper".lower() or user == "2" and computer == "Scissors".lower():
        print "Computer chose scissors : You lost, nice try!"

    elif user.lower() == "Scissors".lower() or user == "3" and computer == "Rock".lower():
        print "Computer chose rock : You lost, nice try!"
    elif user.lower() == "Scissors".lower() or user == "3" and computer == "Paper".lower():
        print "Computer chose paper : You won, great job!"
    elif user.lower() == "Scissors".lower() or user == "3" and computer == "Scissors".lower():
        print "Computer chose scissors : Tie"

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


