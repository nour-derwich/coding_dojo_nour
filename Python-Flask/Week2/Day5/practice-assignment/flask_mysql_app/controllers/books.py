from flask_mysql_app import app
from flask import render_template,redirect,request
from flask_mysql_app.models.book import Book




@app.route('/new_book')
def create_book1():
    list_books = Book.get_all_books()
    return render_template('books.html',  list_books =  list_books)

    
@app.route('/create_book1', methods=['post'])
def book():
    print(request.form)
    data = {
        "title": request.form["title"],
        "num_of_pages": request.form["num_of_pages"]
        
    }
    Book.create_book(data)
    return  redirect('/')
