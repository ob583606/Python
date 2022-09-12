import random

gameLoop = 1

while (gameLoop == 1):

    guessLoop = 1
    inputLoop = 1
    againLoop = 1
    
    print ("Hello and welcome to Ollie's Guessing Game! Please type the end value for the range of numbers you will be guessing in, starting value is always 1.")

    while (inputLoop == 1):
        numError = 1

        try:
            endNumber = int(input())
        
        except ValueError:
            numError = 2
            print ("Sorry bruh not a valid input.")
            
        if (numError == 1):
            if (endNumber < 1):
                print("Please enter a value above 1.")
                
            else:
                inputLoop += 1

    guessNumber = random.randint(1, endNumber)
    
    print ("What an amazing number! The range for this game is 1 -", endNumber, ". Good luck!")

    while (guessLoop == 1):

        print ("Please input your guess!")

        try:
            guess = int(input())

        except ValueError:

            print ("Wow, I thought that you would've learned by now. Fuck you. Stupid idiot.")

        else:

            if (guess > guessNumber):

                print ("Too high! Try again.")

            elif (guess < guessNumber):

                print ("Too low! Try again.")

            else:
                
                guessLoop += 1
        
    while (againLoop == 1):
        print ("Congratulations! You've guessed the number. Play again? (y/n)")
        playAgain = input()

        if (playAgain == "y"):
            againLoop = 2

        elif (playAgain == "n"):
            againLoop = 2
            gameLoop = 2

        else:
            print ("Jesus H. Christ! Smarten up dumbass.")
                
        
            
