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

# Get Only One Row

row = cursor.fetchone()

# If The Row Exists

while row is not None:
    print(row) # Display It
    row = cursor.fetchone() # Get The Next Row
    
# Close Connection

cursor.close()
conn.close()

