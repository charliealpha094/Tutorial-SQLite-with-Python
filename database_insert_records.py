#Done by Carlos Amaral (08/08/2020)

#Insert many records

#Tutorial 3 - How to insert some Records

import sqlite3

#Connect to database
conn = sqlite3.connect('customer.db')


#Create a cursor
c = conn.cursor()


many_customers = [

                    ('Carlos', 'Amaral', 'carlosamaral94@gmail.com'),
                    ('Ana', 'Soares', 'anasoares@gmail.com'),
                    ('Wes', 'Brown', 'wes@brown.com'),
                    ('Mary', 'Holland', 'maryholland@gmail.com'),
                    ('Molly', 'Peters', 'mollypeters@gmail.com')

                ]

c.executemany("INSERT INTO customers VALUES (?,?,?)", many_customers)



print("Command executed successfully...")


#Commit our command
conn.commit()

#Close our connection
conn.close()