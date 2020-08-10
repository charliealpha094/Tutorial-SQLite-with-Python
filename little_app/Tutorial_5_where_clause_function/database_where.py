#Done by Carlos Amaral (10/08/2020)

# Tuturial 5 - Where Clause Function

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


# Add a new record to the table.
def add_one(first, last, email):
    conn = sqlite3.connect('customer.db')
    c = conn.cursor()
    c.execute("INSERT INTO customers VALUES (?,?,?)", (first,last,email))
    #Commit our command
    conn.commit()
    #Close our connection
    conn.close()


# Add many records to table
def add_many(list):
    conn = sqlite3.connect('customer.db')
    c = conn.cursor()
    c.executemany("INSERT INTO customers VALUES (?,?,?)", (list))
    #Commit our command
    conn.commit()
    #Close our connection
    conn.close()

# Delete a record from the table
def delete_one(id):
    conn = sqlite3.connect('customer.db')
    c = conn.cursor()
    c.execute("DELETE from customers WHERE rowid = (?)", id)
    #Commit our command
    conn.commit()
    #Close our connection
    conn.close()


# Lookup with Where
def email_lookup(email):
    conn = sqlite3.connect('customer.db')
    c = conn.cursor()
    c.execute("SELECT * from customers WHERE email = (?)", (email,))
    items = c.fetchall()

    for item in items:
        print(item)

    #Commit our command
    conn.commit()
    #Close our connection
    conn.close()