#Q.6 Cursor is the method to create a cursor and To run SQL commands we use the execute method.  

import mysql.connector
mydb=mysql.connector.connect(
    host="localhost",
    username="abc",
    password="password"
)
mycursor=mydb.cursor()
mycursor.execute("CREATE DATABASE TEST3")
for i in mycursor:
  print(i)
 