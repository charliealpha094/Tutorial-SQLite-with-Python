#Done by Carlos Amaral (10/08/2020)

#Tutorial 2 - Add a record function

import sqlite3 

# Query the database and Return All Records
def show_all():
    # Connect to database
    conn = sqlite3.connect('customer.db')
    # Create a cursor
    c = conn.cursor()

    #Query the Database
    c.execute("SELECT rowid, * FROM customers")
    items = c.fetchall()

    for item in items:
        print(item)

    #Commit our command
    conn.commit()
    #Close our connection
    conn.close()



# Add a new record to the table
def add_one(first,last,email):
    conn = sqlite3.connect('customer.db')
    c = conn.cursor()
    c.execute("INSERT INTO customers VALUES (?,?,?)", (first, last, email))
     #Commit our command
    conn.commit()
    #Close our connection
    conn.close()
