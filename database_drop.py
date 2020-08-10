#Done by Carlos Amaral (09/08/2020)


# Tutorial 13 - Drop (delete) a table

import sqlite3

# Connect to database
conn = sqlite3.connect('customer.db')

# Create a cursor 
c = conn.cursor()


# Drop (delete) a table
c.execute("DROP TABLE customers")
conn.commit()


# Query the Database
c.execute("SELECT rowid, * FROM customers")

items = c.fetchall()

for item in items:
    print(item)

# Commit our command 
conn.commit()

# Close our command
conn.close()

