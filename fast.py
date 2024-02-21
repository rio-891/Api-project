from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from fastapi import Body
import sqlite3


app=FastAPI()

class Book(BaseModel):
    book_id:int
    book_name:str
    author:str
    genre:str

books=[]
#datab_path="book.sqlite"

#def get_db():
#    db_connect=sqlite3.connect("book.sqlite")


@app.get("/book")
def get_all_books():
    connection = sqlite3.connect("book.sqlite") #get_db()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM book_dir")
    books = cursor.fetchall() #stores all the fetched data in books variable
    connection.close()
    return books

@app.post("/book/insert_book", response_model=Book)
def post_insert(book_json_data: dict = Body(...)):
    book = Book(**book_json_data)
    connection = sqlite3.connect("book.sqlite")
    cursor= connection.cursor()

    def insert_items(b:Book): #**
        books.append(b)
        return b
    
    cursor.execute("INSERT into book_dir(book_id,book_name,author,genre) values(?,?,?,?)",(book.book_id, book.book_name, book.author, book.genre),
                   )
    #books= cursor.fetchall()
    connection.close()
    return books

@app.put("/book/{book_id}", response_model=Book)
def put_update(book_id:int,updated_book:Book):
    updated_book=[]
    connection = sqlite3.connect("book.sqlite")
    cursor= connection.cursor()
    if book_id in range(0,len(books)):
        books[book_id]=updated_book
        return updated_book
    else:
        raise HTTPException(status_code=404, detail="page not found")
    
    cursor.execute("UPDATE book_dir set book_id=updated_book[book_id], book_name=updated_book[book_name],author=updated_book[author],genre=updated_book[genre]")
    
@app.delete("/book/{book_id}",response_model=Book)
def delete_items(book_id):
    connection = sqlite3.connect("book.sqlite")
    cursor= connection.cursor()
    if book_id in range(0,len(books)+1):
        delete_itm = books.pop(book_id)
        return delete_itm
        
    else:
        raise HTTPException(status_code=404, detail="Page not found")




  