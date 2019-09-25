from django.shortcuts import render

from django.http import HttpResponse
from .models import Book

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def addBook(request):
    book1 = Book(name ="flying", pageNumber = 10 , genre= "non-fiction", publishDate="1979-01-01" )
    book1.save()
    book2 = Book(name ="purpose", pageNumber = 10 , genre= "non-fiction", publishDate="1980-01-01")
    book2.save()
    return HttpResponse('book added')
def allBook(request):
    bookList = Book.objects.all()
    for eachElement in bookList:
        print(eachElement.name)
    return HttpResponse("all books")

# def printOnly(request):
#     return HttpResponse("print only")
#     bookList = Book.objects.all()
#     if bookList.publishDate > str(2018-01-01):




