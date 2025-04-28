from django.shortcuts import render, redirect
from .models import Book, Review
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView


def home(request):
    return render(request, 'bookapp/home.html')


def books_index(request):
    books = Book.objects.all()
    return render(request, 'bookapp/books/index.html', { 'books': books })



def books_detail(request, book_id):
    book = Book.objects.get(id=book_id)
    return render(request, 'bookapp/books/detail.html', { 'book': book })


def add_review(request, book_id):
    if request.method == 'POST':
        content = request.POST.get('content')
        Review.objects.create(content=content, book_id=book_id)
    return redirect('detail', book_id=book_id)


class BookCreate(CreateView):
    model = Book
    fields = ['title', 'author', 'description', 'published_year']
    success_url = '/books/'
    template_name = 'bookapp/book_form.html'


class BookUpdate(UpdateView):
    model = Book
    fields = ['title', 'author', 'description', 'published_year']
    success_url = '/books/'
    template_name = 'bookapp/book_form.html'


class BookDelete(DeleteView):
    model = Book
    success_url = '/books/'
    template_name = 'bookapp/book_confirm_delete.html'
