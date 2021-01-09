import os
import datetime
import pymysql

# Get username from Gitpod workspace

username = os.getenv("C9_USER")

# Connect to the database

connection = pymysql.connect(host='localhost',
                            user=username, 
                            password='', 
                            db= 'Chinook')

try:
    #run a query
    with connection.cursor() as cursor:
        cursor.execute("DELETE FROM Friends WHERE name = 'Bob';")
        connection.commit()
finally:
    #Close the connection, regardless of success or not
    connection.close()