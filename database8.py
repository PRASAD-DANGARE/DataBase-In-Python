# Python Program To Create Emptab In MYSQL DataBase

'''
Function Name    :  Create Emptab In MYSQL DataBase
Function Date    :  10 Oct 2020
Function Author  :  Prasad Dangare
Input            :  String
Output           :  String
'''

import MySQLdb

# Connect To MySQL DataBase

conn = MySQLdb.connect(host='localhost', database="Enter The Database Name (Schemas)", user='Enter User Name Of Mysql Workbench', password='Enter The Password')

# Prepare A Cursor Object Using Cursor() Method

cursor = conn.cursor()

# Delete Table If Already Exists

cursor.execute("drop table if exists emptab")

# Prepare SQL String To Create A New Table

str = "create table emptab(eno int, ename char(20), sex char(1), salary float)"

# Execute The Query To Create The Table

cursor.execute(str)
print('Table Created...')

# Close Connection

cursor.close()
conn.close()

    
