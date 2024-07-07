import random
print("Guess the number between 1-100! You have 5 chances to try.") 
randomNumber = random.randint(1,100) 
turns = 5

while turns > 0: #check if the guess is correct
    guess = int(input("Please enter a number: "))
    if guess < randomNumber:
        print("Your guess is not correct and lower than the number.")
    elif guess > randomNumber:
        print("Your guess is not corect and higher than the number.")
    else:
        print("Congratulations, your guess is correct!")
        break
    turns -= 1

if turns == 0:
    print("You have used all your chances. The number was:", randomNumber)
      
