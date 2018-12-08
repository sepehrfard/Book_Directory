import sqlite3


"""""

DbConnection: 

This is the command file where connects the GuiController to "book.db" to use sqlite3 database 
to create a book directory and have functions for the directory. These functions are created in 
DbConnection which are called in the GuiController to interact with the database. 

"""""

# name of the database used for book directory
books_db = "my_module/books.db"

# connects to data base and creates columns for the directory
def connect_db():

    # sql command to be executed
    connect_cmd = "CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY, " \
                  "title text,year integer, isbn integer)"

    # connects to specific database
    connect = sqlite3.connect(books_db)

    # executes sql command to create directory
    cursor = connect.cursor()
    cursor.execute(connect_cmd)

    # commits and closes the database connect
    connect.commit()
    connect.close()

# used to insert info into the data base
# takes in four parameters which represent the four labels in the program
def insert(title, author, year, isbn):

    # sql command to insert info
    insert_cmd = "INSERT INTO book VALUES(NULL, ?,?,?,?)"

    # connects to specific database
    connect = sqlite3.connect(books_db)

    # executes sql command to insert in directory
    cursor = connect.cursor()
    cursor.execute(insert_cmd, (title, author, year, isbn))

    # commits and closes the database connect
    connect.commit()
    connect.close()

# used to view all the entries in the directory by rows
def view_all():
    # connects to specific database
    connect = sqlite3.connect(books_db)

    # sql command to view the directory
    view_all_cmd = "SELECT * FROM book"



    # executes sql command to view all the directory
    cursor = connect.cursor()
    cursor.execute(view_all_cmd)

    # retrives return of executed command
    rows = cursor.fetchall()

    # closes connection with database
    connect.close()

    # returns rows to be displayed
    return rows

# searches through directory if any of the four entries have been entered or more than one to
# find a match to return.
def search(title="", author="", year="", isbn=""):

    # sql command to search for given entry
    search_cmd = "SELECT * FROM book WHERE title=? OR author=? OR year=? OR isbn=?"

    # connects to specific database
    connect = sqlite3.connect(books_db)

    # executes sql command to search the directory and return if entry exists
    cursor = connect.cursor()
    cursor.execute(search_cmd, (title, author, year, isbn))

    # fetches the result of sql command
    rows = cursor.fetchall()
    connect.close()

    # returns the selected data from command
    return rows

# after selecting a row the delete function can delete the row from directory and update index
def delete(id):
    # sql command to delete for selected row
    delete_cmd = "DELETE FROM book WHERE id = ?"

    # connects to specific database
    connect = sqlite3.connect(books_db)

    # executes sql code to delete row in directory
    cursor = connect.cursor()
    cursor.execute(delete_cmd, (id,))

    # commits and closes the database connect
    connect.commit()
    connect.close()

# used to update existing entries with new information and updating the database
def update(id, title, author, year, isbn):
    # sql command to update
    update_cmd = "UPDATE book SET title = ?, author = ?, year = ?, isbn = ? WHERE id=?"

    # connects to specific database
    connect = sqlite3.connect(books_db)

    # executes sql to update row with new values
    cursor = connect.cursor()
    cursor.execute(update_cmd, (title, year, author, isbn, id))

    # commits and closes the database connect
    connect.commit()
    connect.close()
