Feature: Book Management System

Scenario: User Sends post request.
Given a user wants to add a book
when the user send post request with data 
then the data added succefully.

Scenario: User Sends get request.
Given a user wants to see  book details
when the user send get request for data 
then the data should be displayed succefully.

Scenario: User Sends update request.
Given a user wants to update a book
when the user send put request with data 
then the data should be updated succefully.

Scenario: User Sends delete request.
Given a user wants to delete a book
when the user send delete request with data 
then the data should be deleted succefully.


