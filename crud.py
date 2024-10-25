#crud opertaions--->

import mysql.connector

#connect to Mysql connector--->
try:
    conn=mysql.connector.connect(
     host="127.0.0.1",
     user="root",
     password="Anand@123",
     database="crud_python"
    )
    mycursor=conn.cursor()
    print("connection Established")
except:
    print("connection lost")

#step2 creating Database--->

# mycursor.execute("create database crud_python")
# conn.commit()

print("database created")
#creating a table---->
# mycursor.execute(
#     """
#     CREATE TABLE customer(
#     id INTEGER PRIMARY KEY,
#     name VARCHAR(50)NOT NULL,
#     email VARCHAR(50)NOT NULL,
#     age INTEGER
#     )"""
# )
# conn.commit()
print("Table is created")

#step4 insert a new record to customer table------>
# mycursor.execute(
# """
#    INSERT INTO customer VALUES
#    (1,"ayush","Ayush@gmail.com",30),
#    (2,"Anand","Anand@gmail.com",24),
#    (3,"Ashwani","Ashwani@gmail.com",25)
# """)
# conn.commit()
#Step5 read Data from the Table---->
mycursor.execute("select * from customer")
myresult=mycursor.fetchall()
# print(myresult)
for x in myresult:
    print(x)

#update data in table---->
 mycursor.execute("update customer set age=14 where id=1")
 conn.commit()
 print("updated")

#delete a table a from the table--->
 mycursor.execute("delete from customer where id=1")
 conn.commit()
 print("record deleted")
