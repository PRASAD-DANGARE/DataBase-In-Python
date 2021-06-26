# Python Program To Retrieve And Display All Rows From The Student Table

'''
Function Name    :  Retrieve And Display All Rows From The Student Table
Function Date    :  9 Oct 2020
Function Author  :  Prasad Dangare
Input            :  String
Output           :  It Display All Data In student table
'''

import MySQLdb

# Connect To MYSQL Database

conn = MySQLdb.connect(host='localhost', database="Enter The Database Name (Schemas)", user='Enter User Name Of Mysql Workbench', password='Enter The Password')

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
    print(row) # Display Each Row
    
# Close Connection

cursor.close()
conn.close()

