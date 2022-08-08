#!/usr/bin/python3

import mysql.connector
import cgi

print("content-type:text/html")
print("Access-Control-Allow-Origin: *")
print()

form_values = cgi.FieldStorage()
uname = form_values.getvalue("uname")
lname = form_values.getvalue("lname")


#Connecting to database
DB = mysql.connector.connect(
    host="db",
    port=3306,
    database="dba",
    user="root",
    password="kela"
)

mycursor = DB.cursor()

#Inserting data
sql = "INSERT INTO tba (name, surname) VALUES (%s, %s)"
val = [
    (uname, lname),
]

mycursor.executemany(sql, val)
DB.commit()

print("Query OK, Data Inserted!")
