# Python Program To Increase The Salary Of An Employee By Accepting The Employee Number From KeyBoard

'''
Function Name    :  Increase The Salary Of An Employee From KeyBoard
Function Date    :  10 Oct 2020
Function Author  :  Prasad Dangare
Input            :  String
Output           :  String
'''

import MySQLdb

# Function To Store Row Into The Employee Table

def update_rows(eno):
    
    # Connect To MySQL DataBase
    
    conn = MySQLdb.connect(host='localhost', database="Enter The Database Name (Schemas)", user='Enter User Name Of Mysql Workbench', password='Enter The Password')

    # Prepare A Cursor Object Using Cursor() Method

    cursor = conn.cursor()
    
    # Prepare SQL Query To Update The Salary In A Row
    
    str = "update student set salary = salary+1000 where eno = '%d' "
    
    # Define The Arguments
    
    args = (eno)
    try:
        
        # Execute The SQL Query Using execute() method
        
        cursor.execute(str % args) 
        
        # Save The Changes To The DataBase
        
        conn.commit()
        print('1 Row Updated...')
        
    except:
        
        # RollBack If There Is Any Error
        
        conn.rollback()
        
    finally:
        
        # Close Connection
        
        cursor.close()
        conn.close()
        
# Enter Employee Number Whose Row Is To Be Updated

x = int(input('Enter ENO : '))

# Pass eno To update_rows() Function

update_rows(x)

        
        
    
