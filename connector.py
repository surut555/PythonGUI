#เชื่อต่อฐานข้อมูล mysql
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database= "mydatabase"
)
#สร้างตารางฐานข้อมูล
mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")

