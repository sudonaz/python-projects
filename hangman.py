import random

#define word list, turns and guesses
words = ["right", "bicycle", "computer", "calculator", "password", "volleyball", "chicken", "biology"]
secretWord = random.choice(words)
turns = 10
guesses = "" #an empty string to store the user's guesses


#check if the user has any turns, if there are any turns enter the loop
while turns > 0:
    failed = 0
    
    for char in secretWord: #Loop for each letter in the secretWord
        if char in guesses:
            print (char, end = " ")
        else:
            print("_")
            failed += 1

    if failed == 0:
        print("You won!")
        print("The word is: ", secretWord)
        break

    guess = input("Please enter a letter: ")
    guesses += guess

    if guess not in secretWord:
        turns -= 1
        print("This letter is not found in the word")
        print("You have", turns, "more guesses")
        if turns == 0:
            print("You loose, please try again")
