from django.shortcuts import render, redirect
from .forms import AuthorForm, BookForm, RatingsForm

def author(request):
    template = "bookstore/form.html"
    form = AuthorForm()
    return render(request, template, {"form": form, "title": "Add An Author", "url": "add-author"})


def add_author(request):
    if request.method == "POST":
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('author')
    

def book(request):
    template = "bookstore/form.html"
    form = BookForm()
    return render(request, template, { "form": form, "title": "Add A Book", "url": "add-book" })


def add_book(request):
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('book')
    
    
def rating(request):
    template = "bookstore/form.html"
    form = RatingsForm()
    return render(request, template, { "form": form, "title": "Rate A Book", "url": "add-rating" })


def add_rating(request):
    if request.method == "POST":
        form = RatingsForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('ratings')