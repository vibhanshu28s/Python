# 2 functions - add, add_condition and remove
import mysql.connector
#---------------------------------------------------------------------------------------------------------------
def add_task():
  mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="vibhanshu",
    database="schedule"
  )

  mycursor = mydb.cursor()

  sql = "INSERT INTO schedule1 (Details,Description,Quantity,Priority) VALUES (%s, %s, %s, %s)"



  Details=input("\nEnter Details ")
  Description=input("Enter Description ")
  Quantity=int(input("Enter Quantity "))
  Priority=int(input("Enter Priority "))

  mycursor.execute(sql, (Details,Description,Quantity,Priority))

  mydb.commit()

  print()
  print(mycursor.rowcount, "record inserted.")

  conti=input("Press Enter to Return TO main Screen and 0 to Exit: ")
  if conti=="0":
      exit_program()
  else:
    main_scr()

def remove_task():
  mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="vibhanshu",
    database="schedule"
  )

  select_type_for_func()

  id_to_delete = int(input("\nEnter the Sr.NO. of the record to delete: "))
  sql = "DELETE FROM schedule1 WHERE Sr_No = %s"
  val = (id_to_delete,)  # note the comma

  mycursor = mydb.cursor()
  mycursor.execute(sql, val)
  mydb.commit()

  print()
  print(mycursor.rowcount, "record deleted.")

  conti=input("\nPress Enter if you want to continue or Enter 0 to Exit to Home Screen: ")
  if conti=="0":
    main_scr()
  else:
    sort_by_priority_for_func()
    remove_task()


def add_condition():
  condition=input("Press Enter to Continue and 0 Exit ")
  if(condition=="0"):
    main.main_scr()
  else:
    add_task()

#---------------------------------------------------------------------------------------------------------------

def update_task():

  mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="vibhanshu",
    database="schedule"
  )

  select_type_for_func()
  id_to_update = int(input("\nEnter the Sr.No. of the record to update or Press 0 to Exit to Home Screen: "))
  if id_to_update==0:
    main_scr()

  else:
    mycursor = mydb.cursor()
    print("----------------------------------------------Column To Update --------------------------------------------------"
          "\n\t\t\t\t\t\t\t\t\t\t\t\t1.Details"
          "\n\t\t\t\t\t\t\t\t\t\t\t\t2.Description"
          "\n\t\t\t\t\t\t\t\t\t\t\t\t3.Quantity"
          "\n\t\t\t\t\t\t\t\t\t\t\t\t4.Priority")


    column_number=int(input("Select Column Name: "))

    if column_number==1:
      col ="Details"


    elif column_number == 2:
      col = "Description"


    elif column_number == 3:
      col = "Quantity"


    elif column_number == 4:
      col = "Priority"

    elif column_number == 5:
      main_scr()



    new_value = input(f"Enter new value for {col}: ")
    sql = f"UPDATE schedule1 SET {col} = %s WHERE Sr_No = %s"
    val = (new_value, id_to_update)

    mycursor.execute(sql, val)
    mydb.commit()
    conti=input("\nPress Enter to return to Update Task or Enter 0 to Exit to MainScreen: ")
    if conti=="0":
        main_scr()
    else:
        update_task()


def update_condition():
  option=input("Press Enter to continue 0 to Exit ")
  if option=="0":
    exit_program()
  else:
    update_task()

#---------------------------------------------------------------------------------------------------------------

def view_task_for_func():
  mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="vibhanshu",
    database="schedule"
  )

  mycursor = mydb.cursor()
  mycursor.execute("SELECT * FROM SCHEDULE1")

  for data in mycursor:
      print(data)



def sort_by_priority_for_func():
  mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="vibhanshu",
    database="schedule"
  )

  mycursor = mydb.cursor()
  mycursor.execute("SELECT * FROM SCHEDULE1 ORDER BY PRIORITY")

  for data in mycursor:
    print(data)


def select_type_for_func():
  y_n=input("Want to see List priority wise (Y/N) ")
  if(y_n=="Y") or (y_n=="y"):
    sort_by_priority_for_func()
  else:
    view_task_for_func()
#---------------------------------------------------------------------------------------------------------------

def view_task():
  mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="vibhanshu",
    database="schedule"
  )

  mycursor = mydb.cursor()
  mycursor.execute("SELECT * FROM SCHEDULE1")

  for data in mycursor:
      print(data)

  conti = input("\nPress Enter to Continue and 0 To Return To Home Screen: ")
  if conti == 0:
    main_scr()
  else:
    view_task()


def sort_by_priority():
  mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="vibhanshu",
    database="schedule"
  )

  mycursor = mydb.cursor()
  mycursor.execute("SELECT * FROM SCHEDULE1 ORDER BY PRIORITY")

  for data in mycursor:
    print(data)

  conti = input("\nPress Enter to Continue To Home Screen: ")
  if conti =="":
    main_scr()


def select_type():
  y_n=input("Want to see List priority wise (Y/N) ")
  if(y_n=="Y") or (y_n=="y"):
    sort_by_priority()
  else:
    view_task()

def exit_program():
  print("Exiting! Have a nice day!")

#---------------------------------------------------------------------------------------------------------------

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

#---------------------------------------------------------------------------------------------------------------

# Main Screen #

def main_scr():


    print("-------------------------------------------------- Content ----------------------------------------------------")
    print("\t\t\t\t\t\t\t\t\t\t\t\t1.Add Task\n\t\t\t\t\t\t\t\t\t\t\t\t2.Update Task\n\t\t\t\t\t\t\t\t\t\t\t\t3.View Task"
          "\n\t\t\t\t\t\t\t\t\t\t\t\t4.Remove Task""\n\t\t\t\t\t\t\t\t\t\t\t\t5.Exit")
    print("---------------------------------------------------------------------------------------------------------------")

    input_choice=int(input("\nEnter Choice "))



    if (input_choice==1):
        add_task()
    elif(input_choice==2):
        update_condition()
    elif(input_choice==3):
        select_type()

    elif(input_choice==4):
        remove_task()

    elif(input_choice==5):
        feedback()
        exit_program()

main_scr()