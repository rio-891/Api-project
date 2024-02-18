from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import sqlite3


app=FastAPI()

class Book(BaseModel):
    book_id:int
    book_name:str
    author:str
    genre:str

books=[]
#datab_path="book.db"

#def get_db():
#    db_connect=sqlite3.connect("books.db")


@app.get("/book")
def get_all_books():
    connection = sqlite3.connect("book.db") #get_db()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM books")
    books = cursor.fetchall() #stores all the fetched data in books variable
    connection.close()
    return books

@app.post("/book")
def post_insert():
    #connection = sqlite3.connect("book.db")
    #cursor= connection.cursor()
    def insert_items(b:Book):
        books.append(b)
        return b
    
@app.put("/book/{book_id}", response_model=Book)
def put_update(book_id:int,updated_book:Book):
    for book_id in range(0,len(books)+1):
        books[book_id]=updated_book
        return updated_book
        break
    else:
        raise HTTPException(status_code=404, detail="page not found")
    
@app.delete("/books/{books_id}",response_model=Book)
def delete_items(book_id):
    for book_id in range(0,len(books)+1):
        delete_itm = books.pop(book_id)
        return delete_itm
        break
    else:
        raise HTTPException(status_code=404, detail="Page not found")




  