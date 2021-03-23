import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="Ollie",
  password="583606Banana",
  database="highscores"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM high_scores")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)
