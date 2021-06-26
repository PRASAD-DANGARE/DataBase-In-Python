# Python Program To Delete A Row From student Table By Accepting The Student eno number

'''
Function Name    :  Delete A Row From student Table Using eno
Function Date    :  10 Oct 2020
Function Author  :  Prasad Dangare
Input            :  String
Output           :  String
'''

import MySQLdb

# Function To Store Row Into The Student Table

def delete_rows(eno):
    
    # Connect To MySQL DataBase
    
    conn = MySQLdb.connect(host='localhost', database="Enter The Database Name (Schemas)", user='Enter User Name Of Mysql Workbench', password='Enter The Password')

    # Prepare A Cursor Object Using Cursor() Method

    cursor = conn.cursor()
    
    # Prepare SQL Query String To Delete A Row
    
    str = "delete from student where eno = '%d' " 
    
    # Define The Arguments
    
    args = (eno)
    try:
        
        # Execute The SQL Query Using execute() method
        
        cursor.execute(str % args)
        
        # Save The Changes To The DataBase
        
        conn.commit()
        print('1 Row Deleted...')
        
    except:
        
        # RollBack If There Is Any Problem
        
        conn.rollback()
        
    finally:
        
        # Close Connection
        
        cursor.close()
        conn.close()
        
# Enter Student Number Whose Row Is To Be Deleted

x = int(input("Enter eno : "))

# Pass eno To delete_rows() Function

delete_rows(x)
