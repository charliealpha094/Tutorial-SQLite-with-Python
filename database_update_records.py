#Done by Carlos Amaral (09/08/2020)


# Tutorial 8 - Update Records

import sqlite3

#Connect to database
conn = sqlite3.connect('customer.db')


#Create a cursor
c = conn.cursor()



#Update Records

c.execute("""UPDATE customers SET first_name = 'Tereza'
            WHERE last_name = 'Holland'

    """)

conn.commit()



#Query the database
c.execute("SELECT rowid, * FROM customers")

items = c.fetchall()

for item in items:
    print(item)


#Commit our command 
conn.commit()

#Close our command 
conn.close()