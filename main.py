from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from fastapi import Body
import uvicorn
#import sqlite3


app=FastAPI()

class Book(BaseModel):
    book_id:int
    book_name:str
    author:str
    genre:str

data=[]
@app.post("/book/insert_book")
async def insert_book(book:Book,ins:int):#creating an object
    ins = data.append(book.dict())
    return ins 
@app.get("/book")
async def select_items():
    return data
@app.put("/book/{book_id}")
async def update_items(book_id:int,upd,book:Book):
    upd=data[book_id-1]=book
    return upd

@app.delete("/book")
async def del_iems(book_id:int,delt,book:Book):
   delt= data.pop(book_id-1)#though the value of id is 1, but by def intendation starts with 0.
   return delt
