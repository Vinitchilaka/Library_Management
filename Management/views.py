from django.shortcuts import render
from Management.models import *

def welcome_page(req):
    return render(req, template_name="welcome.html")

def Add_book(req):
    message = ""
    if req.method == 'POST':
        formdata = req.POST

        bkid = formdata.get('id')
        Books = Book.objects.filter(id=bkid).first()

        if formdata:
            if not Books:
                Books = Book(book_name = formdata.get('book_name'),
                             book_author = formdata.get('book_author'),
                             book_isbn = formdata.get('book_isbn'),
                             book_category = formdata.get('book_category'))
                if int(bkid):
                    Books.id = bkid
                Books.save()
                message = 'BOOK IS ADDED IN SYSTEM.'
            else:
                Books.book_name = formdata.get('book_name')
                Books.book_author = formdata.get('book_author')
                Books.book_isbn = formdata.get ('book_isbn')
                Books.book_category = formdata.get('book_category')
                Books.save()
                message = 'BOOK IS UPDATED IN SYSTEM.'
    return render(req, template_name="Add_Book.html", context={"result":message, 'book': Book(id='',book_name='',book_author='',book_isbn='',book_category='')})

def Book_list(req):
    Book_list = Book.objects.all()
    return render(req, template_name="Book_list.html", context = {"Book_list":Book_list})

def Edit_book(req,bkid):
    book = Book.objects.get(id=bkid)
    return render(req, template_name="Add_Book.html", context={"book":book})

def Delete_book(req,bkid):
    Books = Book.objects.get(id=bkid)
    Books.delete()
    Book_list = Book.objects.all()
    return render(req, template_name="Book_list.html", context={"Book_list":Book_list})

