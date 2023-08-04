from random import choice
while True:
    print """
Welcome to Hangman! A word will be chosen at random 
and, you must try to guess the word correctly letter 
by letter, before you run out of attempts. Good luck!\n"""

    player1 = raw_input("What is your name Player 1? ")
    print "Hello, {}! Welcome to Hangman!".format(player1)

    print "\n"
    print "Start guessing..."
    word = choice(["elephant", "apple", "artist", "elite",
                   "dictionary", "dinosaur", "hangman", "legendary",
                   "inventory", ]).lower()
    guesses = ''
    turns = 10
    while turns > 0:
        failed = 0
        for char in word:   
            if char in guesses:
                print char,
            else:
                print "_",
                failed += 1
        if failed == 0:
            print "\nYou won!"
            break
        print
        guess = raw_input("Guess a character:\t")
        guesses += guess
        if guess not in word:
            turns -= 1
            print "Incorrect\n"
            print "You have", + turns, 'guesses left.'
            if turns == 0:
                print "You Lose!\n"
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

