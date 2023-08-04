player1 = raw_input("What is your name Player 1? ")
print "Hello, {}! Welcome to Hangman!".format(player1)

print "\n"
print "Start guessing..."
word = "hockey"
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
        print "\nYou won"
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
