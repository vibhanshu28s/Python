import mysql.connector

def feedback():
  mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="vibhanshu",
    database="schedule"
  )

  mycursor = mydb.cursor()

  sql = "INSERT INTO feedback (Rating_out_5,Description) VALUES (%s, %s)"

  Rating_out_5 = input("\nEnter Rating out of 5 ")
  Description = input("Enter Description ")

  mycursor.execute(sql, (Rating_out_5, Description))

  mydb.commit()

  print()
  print("Thanks For Feedback!")

feedback()