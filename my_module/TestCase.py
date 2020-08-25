import sqlite3
import os.path as path
import os

"""""
Test case is checking the function which creates a sqlite database with name test.db then checks 
if file was created with the same name using (os.path).

- Checks if file exists, if file exists the correct statement is printed and the file is deleted 
to show the ability of creating a file every time this script is ran. 

"""""

# name of the database used for test directory
test_db = "test.db"

# connects to data base and creates columns for the directory
def connect_db():

    # sql command to be executed
    connect_cmd = "CREATE TABLE IF NOT EXISTS test (id INTEGER PRIMARY KEY, " \
                  "title text,year integer, isbn integer)"

    # connects to specific database
    connect = sqlite3.connect(test_db)

    # executes sql command to create directory
    cursor = connect.cursor()
    cursor.execute(connect_cmd)

    # commits and closes the database connect
    connect.commit()
    connect.close()

# running the file to create the database file
connect_db()

# checking if the file was created and exists with in the directory
if path.isfile(test_db):
    # message printed only if file exists
    print('File created and file will be deleted for the next check')
    os.remove(test_db)
else:
    # message printed if file was not created
    print('File was not created and does not exist')



