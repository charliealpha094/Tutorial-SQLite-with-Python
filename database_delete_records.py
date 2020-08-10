#Done by Carlos Amaral (09/08/2020)


# Tutorial 9 - Delete Records

import sqlite3 


#Connect to database
conn = sqlite3.connect('customer.db')


#Create a cursor
c = conn.cursor()



#Delete Records
c.execute("DELETE from customers WHERE rowid = 3")

conn.commit()


#Query the database
c.execute("SELECT rowid, * FROM customers")

items = c.fetchall()

for item in items:
    print(item)

# Commit our command
conn.commit()

#Close our command 
conn.close()