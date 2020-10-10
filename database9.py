# Python Program Using GUI To Retrieve A Row From A MYSQL DataBase Table

'''
Function Name    :  GUI To Retrieve A Row From A MYSQL DataBase Table
Function Date    :  10 Oct 2020
Function Author  :  Prasad Dangare
Input            :  In This Program We Can Search Employee Name By Just Typing Its eno Number.
Output           :  In Output New Window Is Opened Where We Can Find Name By Its ENO 
'''

import MySQLdb
from tkinter import*

# Create Root Window

root = Tk()

# A Function That Takes Employee Number And Display The Row

def retrieve_rows(eno):
    
    # Connect To MYSQL DataBase
    
    conn = MySQLdb.connect(host='localhost', database="pythondb", user='prasadD', password='prasadD@93')

    # Prepare A Cursor Object Using Cursor() Method

    cursor = conn.cursor()
    
    # Prepare SQL Query String To Retrieve A Row
    
    str = "select * from emptab where eno = '%d' "
    
    # Define The Arguments
    
    args = (eno)
    
    # Execute The SQL Query Using execute() method
    
    cursor.execute(str % args)
    
    # Get Only One Row
    
    row = cursor.fetchone()
    
    # If The Row Exists Display It Using A Label
    
    if row is not None:
        lbl = Label(text = row, font = ('Arial', 14)).place(x=50, y=200)
        
    # Close Connection
    
    cursor.close()
    conn.close()
    
# A Function That Takes Input From Entry Widget

def display(self):
    
    # Retrieve That Value From Entry Widget
    
    str = e1.get()
    
    # Display The Value From The Entry Widget
    
    lbl = Label(text = 'You Entered : '+str, font=('Arial', 14)).place(x=50, y=150)
    
    # Call The Function That Retrieves The Row
    
    retrieve_rows(int(str))
    
# Create A Frame As Child To Root Window

f = Frame(root, height=350,width=600)

# Let The Frame Will Not Shrink

f.propagate(0)

# Attach The Frame To Root Window

f.pack()

# Label

l1 = Label(text='Enter Employee Number : ', font=('Arial', 14))

# Create Entry Widget For Accepting Employee Number

e1 = Entry(f, width=15, fg='red', bg='yellow', font=('Arial', 14))

# When User Presses Enter , Bind That Event To Display Method

e1.bind("<Return>", display)

# Place Label  And Entry Widgets In The Frame

l1.place(x=50, y=100)
e1.place(x=300, y=100)

# Handle The Events

root.mainloop()