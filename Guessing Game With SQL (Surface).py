import random
import mysql.connector

## Connects to the SQL server. Assumedly will stall the program for about a minute and then produce an error message if the server isn't available. ##
mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="583606Banana",
        database="high_scores"
    )


gameLoop = 1
## Beginning of the loop that holds all of the game's code. ##
while (gameLoop == 1):
    guessLoop = 1
    inputLoop = 1
    againLoop = 1
    playerGuesses = 0
    
    playerName = input("Hello and welcome to Ollie's Guessing Game! Please type your name.")
    print ("Such a beautiful name! One of my favourites. Please type the upper bound for the range of numbers you will be guessing in, lower bound is always 1.")

## This loop runs through the steps of the user choosing a number until it is using the correct formatting. ##
    while (inputLoop == 1):
        numError = 1

        try:
            endValue = int(input())
        
        except ValueError:
            numError = 2
            print ("Sorry friend, not a valid input! Please only use whole numbers!")
            
        if (numError == 1):
            if (endValue < 1):
                print("Please enter a value > 1.")
                
            else:
                inputLoop += 1

    guessNumber = random.randint(1, endValue)
    
    print ("What an amazing number! The range for this game is 1 -", endValue, ". Good luck!")

    while (guessLoop == 1):
        try:
            guess = int(input("Please input your guess!"))

        except ValueError:
            print ("Sorry friend, not a valid input! Please only use whole numbers!")

        else:
            playerGuesses += 1
            if (guess > guessNumber):
                print ("Too high! Try again.")

            elif (guess < guessNumber):
                print ("Too low! Try again.")

            else:
                guessLoop += 1
## Sends all recorded information to the server running off of my Surface. ##
    mycursor = mydb.cursor()

    mycursor.execute("INSERT INTO high_scores (Name,EndValue,Guesses) VALUES ('%s', %d, %d)" % (playerName, endValue, playerGuesses))

    mydb.commit()

    mycursor.execute("SELECT * FROM high_scores")

    myresult = mycursor.fetchall()

    for x in myresult:
        print(x)
    
    while (againLoop == 1):
        playAgain = input("Congratulations! You've guessed the number. Play again? (y/n)")

        if (playAgain == "y"):
            againLoop = 2

        elif (playAgain == "n"):
            againLoop = 2
            gameLoop = 2

        else:
            print ("There was only two options, and you managed to screw it up. Nice going.")
                
        
            
