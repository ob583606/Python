import random
import mysql.connector

## Just so that I don't need one python file for a PC version and one for a Surface version. ##
playerPlatform = input("Please type 'p' for PC, or anything else for Surface.") 
if playerPlatform == "p":
    playerPlatform = "10.0.0.120"
else:
    playerPlatform = "localhost"

## Connects to the SQL server. Assumedly will stall the program for about a minute and then produce an error message if the server isn't available. ##
mydb = mysql.connector.connect(
        host="%s" % (playerPlatform),
        user="Ollie",
        password="583606Banana",
        database="high_scores"
    )
mycursor = mydb.cursor()


gameLoop = 1
## Beginning of the loop that holds all of the game's code. ##
while (gameLoop == 1):
    guessLoop = 1
    inputLoop = 1
    againLoop = 1
    playerGuesses = 0

    ## Displays the high scores. ##
    print("High score!")
    
    mycursor.execute("SELECT Name, Guesses, EndValue AS 'Score' FROM high_scores WHERE EndValue=(select max(EndValue) from high_scores);")

    myresult = mycursor.fetchall()

    for x in myresult:
        print(x)
    
    playerName = input("Hello and welcome to Ollie's Guessing Game! Please type your name.")

## This loop runs through the steps of the user choosing a number until it is using the correct formatting. Similar styles are used throughout the program, I debated defining a function for this purpose but decided nah. ##
    while (inputLoop == 1):
        numError = 1

        try:
            endValue = int(input("Such a beautiful name! One of my favourites. Please type the upper bound for the range of numbers you will be guessing in, lower bound is always 1."))
        
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
    mycursor.execute("INSERT INTO high_scores (Name,EndValue,Guesses) VALUES ('%s', %d, %d)" % (playerName, endValue, playerGuesses))

    mydb.commit()
    
    while (againLoop == 1):
        playAgain = input("Congratulations! You've guessed the number. Play again? (y/n)")

        if (playAgain == "y"):
            againLoop = 2

        elif (playAgain == "n"):
            againLoop = 2
            gameLoop = 2

        else:
            print ("There was only two options, and you managed to screw it up. Nice going.")
