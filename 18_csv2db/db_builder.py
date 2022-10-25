#Clyde "Thluffy" Sinclair
#SoftDev  
#skeleton/stub :: SQLITE3 BASICS
#Oct 2022

import sqlite3   #enable control of an sqlite database
import csv       #facilitate CSV I/O

DB_FILE="students.db"

db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
c = db.cursor()               #facilitate db ops -- you will use cursor to trigger db events
# c.execute("CREATE TABLE students(name TEXT, age INTEGER, id INTEGER PRIMARY KEY)")


with open('students.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    # for row in reader:
    #     c.execute("INSERT INTO students VALUES (" + row['name'] + ", " + row['age'] + "," + row['id'] + ")")
    # c.execute("SELECT * FROM students")

value = c.execute("SELECT * FROM students")
value2 = value.fetchone()
value2 = value.fetchone()

print(value2)


#==========================================================


# < < < INSERT YOUR TEAM'S POPULATE-THE-DB CODE HERE > > >


command = ""          # test SQL stmt in sqlite3 shell, save as string
c.execute(command)    # run SQL statement

#==========================================================

db.commit() #save changes
db.close()  #close database


