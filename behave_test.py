from behave import given,when,then
from fast import app
import json
from fastapi import testclient

client = testclient(app)
@given('a user wants to add a book')
def user_add_book(text):#here i created text as object container to hold data usefull for all the senarios.
    text.books = {#books contain all the attributes and is within text
        "book_id": 1,
        "book_name":"Api creation",
        "author":"bhargav",
        "genre":"horror"
    }

@when('the user send post request with data')
def user_post_request(text):
    response = client.post("/book/insert_book" json=text.books)
    text.response = response

@then('the book added successfully')
def book_added_succ(text):
    assert text.response.status_code == 200 #assert- check weather status code is 200(successful)
