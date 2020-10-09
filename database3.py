# Python Program To Retrieve All Rows From Student Table And Display The Column Values In Tabular Form

'''
Function Name    :  Display All Rows Of Student Table
Function Date    :  9 Oct 2020
Function Author  :  Prasad Dangare
Input            :  String
Output           :  It Display Only Values Of student table 
'''

import MySQLdb

# Connect To MYSQL Database

conn = MySQLdb.connect(host='localhost', database="pythondb", user='prasadD', password='prasad@93')

# Prepare A Cursor Object Using Cursor() Method

cursor = conn.cursor()

# Execute A SQL Query Using Execute() Method

cursor.execute("select * from student")

# Get All Rows

rows = cursor.fetchall()

# Display The Number Of Rows

print('Total Number Of Rows = ', cursor.rowcount)

# Display The Rows From Rows Object

for row in rows:
    eno = row[0]
    name = row[1]
    salary = row[2]
    print('%-6d %-15s %10.2f' %(eno, name, salary))
    
# Close Connection

cursor.close()
conn.close()

