import random
programLoop = 0
spc = ("     ") 

while (programLoop != "n"):
    gridLoop = 0
    gridLength = input("Please type the number of variables for your matrix.")
    gridWidth = input("Please type the number of rows for your matrix.")

    try:
        gridLength = int(gridLength)
        gridWidth = int(gridWidth)
    
    except ValueError:
        print("Sorry, one or more inputs were invalid.")

    if (isinstance(gridLength, int) == True and isinstance(gridWidth, int) == True):
        while (gridLoop < gridWidth):

            c = random.randint(0, 9)
            w = random.randint(0, 9) 
            x = random.randint(0, 9)
            y = random.randint(0, 9)
            z = random.randint(0, 9)
            
            if (gridLength == 1):

                print(x, spc, c)
                gridLoop += 1

            if (gridLength == 2):

                print(x, spc, y, spc, c)
                gridLoop += 1

            if (gridLength == 3):

                print(x, spc, y, spc, z, spc, c)
                gridLoop += 1

            if (gridLength == 4):

                print(w, spc, x, spc, y, spc, z, spc, c)
                gridLoop += 1
            
    programLoop = input("Would you like a new matrix? Default = yes, n for no.")