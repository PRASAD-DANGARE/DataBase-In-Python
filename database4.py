# Python Program To Insert A Row A Table In MySQL

'''
Function Name    :  Insert A Row A Table In MySQL
Function Date    :  9 Oct 2020
Function Author  :  Prasad Dangare
Input            :  String
Output           :  String
'''

import MySQLdb

# Connect To MYSQL Database

conn = MySQLdb.connect(host='localhost', database="pythondb", user='prasadD', password='prasadD@93')

# Prepare A Cursor Object Using Cursor() Method

cursor = conn.cursor()

# Prepare SQL Query String To Insert A Row

str = "insert into student(eno, name, salary) values(5005, 'Varad', 5000)"

try:
    
    # Execute The SQL Query Using Execute() Method
    
    cursor.execute(str)
    
    # Save The Changes To The Database
    
    conn.commit(str)
    print('1 Row Inserted...')
    
except:
    
    # RollBack If There Is Any Error
    
    conn.rollback()
    
# Close Connection

cursor.close()
conn.close()
