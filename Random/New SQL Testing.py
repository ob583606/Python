import mysql.connector

Name = input("Name pwease")
EndValue = int(input("End Value"))
Guesses = int(input("Guesses"))

mydb = mysql.connector.connect(
  host="10.0.0.120",
  user="Ollie",
  password="583606Banana",
  database="high_scores"
)

mycursor = mydb.cursor()

mycursor.execute("INSERT INTO high_scores (Name,EndValue,Guesses) VALUES ('%s', %d, %d)" % (playerName, endValue, playerGuesses))

mydb.commit()

mycursor.execute("SELECT * FROM high_scores")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)
