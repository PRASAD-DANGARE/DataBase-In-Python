# Python Program To Insert Several Rows Into A Table From The Keyboard

'''
Function Name    :  Insert Several Rows Into A Table From The Keyboard
Function Date    :  10 Oct 2020
Function Author  :  Prasad Dangare
Input            :  String
Output           :  String
'''

import MySQLdb

# Function To Store Row Into The Student Table

def insert_rows(eno, name, salary):
    
    # Connect To MySQL DataBase
    
    conn = MySQLdb.connect(host='localhost', database="pythondb", user='prasadD', password='prasadD@93')

    # Prepare A Cursor Object Using Cursor() Method

    cursor = conn.cursor()
    
    # Prepare SQL Query String To Insert A Row
    
    str = "insert into student(eno, name, salary) values('%d', '%s', '%f')"
    
    # Define The Arguments
    
    args = (eno, name, salary)
    
    try:
        
        # Execute The SQL Query Using Execute() Method
        
        cursor.execute(str % args)
        
        # Save The Changes To The DataBase
        
        conn.commit()
        print('1 Row Inserted...')
        
    except:
        
        # RollBack If There Is Any Error
        
        conn.rollback()
        
    finally:
        
        # Close Connection
        
        cursor.close()
        conn.close()
        
# Enter Rows From KeyBoard

n = int(input('How Many Rows ? '))

for i in range(n):
    x = int(input('Enter eno : '))
    y = input('Enter Name : ')
    z = float(input('Enter Salary : '))
    
    # Pass eno, name, salary To insert_rows() Function
    
    insert_rows(x, y, z)
    print('--------------------')
    