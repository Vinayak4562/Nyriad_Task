import sqlite3

connection = sqlite3.connect("Store_transaction.db")  #connection is use to connect the DB

cursor = connection.cursor()                     # cursor is used to interact with the DB through SQL commands

# To Create a store table
command1 = """ CREATE TABLE IF NOT EXISTS stores(store_ID INTEGER PRIMARY KEY, location TEXT )"""
cursor.execute(command1)

# To Create a Purchase table
command2 = """ CREATE TABLE IF NOT EXISTS 
purchages(purchase_ID INTEGER PRIMARY KEY, store_ID INTEGER, total_cost FLOAT,
FOREIGN KEY(store_ID) REFERENCES stores(store_ID))"""

cursor.execute(command2)

#Add to store
cursor.execute("INSERT INTO stores VALUES(21,'minnepolis,MN')")
cursor.execute("INSERT INTO stores VALUES(95,'chicago,IL')")
cursor.execute("INSERT INTO stores VALUES(64,'IOW city,IA')")

#Add to purchase
cursor.execute("INSERT INTO purchages VALUES(54,21,15.49)")
cursor.execute("INSERT INTO purchages VALUES(23,64,21.12)")

# Get result
cursor.execute("SELECT * FROM purchages")
result = cursor.fetchall()
print(result)

# Update 
cursor.execute("UPDATE purchages SET total_cost = 3.67 WHERE purchase_ID = 54")