def hangman_game():
    name = input("What is your name? ")
    print("Hello " + name, "It is time to play hangman")
    print("Start guessing...")
    # determine the number of turns
    turns = 10
    # creates a variable with an empty value
    guesses = " "
    # here we set the secret
    word = "secret"
    while turns > 0:
        failed = 0
        for char in word:
            if char in guesses:
                print(char)
            else:
                print("_")
                failed += 1
        if failed == 0:
            print("You won!")
            break
        guess = input("Guess a character: ")
        guesses += guess
        if guess not in word:
            turns -= 1
            print("Wrong guess")
        print("You have ", + turns, "more guesses")
        if turns == 0:
            print("Game is over. You lost")
    check = input("Do you want to play again Y/N? ")
    if check == "Y":
        hangman_game()
    else:
        print("Goodbye")

hangman_game()

