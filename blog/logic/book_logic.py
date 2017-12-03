# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.http import HttpResponse
from blog.models.book import Book
__author__ = 'May25th'


def get_book_list(request):
    # 更简单的实现
    books = Book.objects.order_by('name')
    return render_to_response('book_list.html', {'books': books})


def add_book(request):
    book = Book(t_id='xueliehuax', name='Time Book')
    book.save()
    return HttpResponse(book.name)
