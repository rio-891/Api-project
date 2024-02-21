import sqlite3

def create_tables():  #creating a database name book.sqlite
    connection = sqlite3.connect('book.sqlite') #creating a connection with sqlite3
    cursor = connection.cursor()
    
#creting table , columns
    cursor.execute(""" 
    create table book_dir(
                   book_id int not null primary key,
                   book_name text not null,
                   author text not null,
                   genre text not null
    )
""")
    

    connection.commit()
    connection.close()


  # when we want just lines of specific code to be executes, we use this.
create_tables()




#the database is created, connection been created, cursor is been created(so that we can easly manipulate the data using insert, update ,delete.)
#created columns, when we execute, the changes are in a transaction and after we use commit, the changes are been made, then we close the connection.
    