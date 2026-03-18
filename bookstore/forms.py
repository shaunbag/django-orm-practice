from django import forms
from .models import Author, Book, Rating

class AuthorForm(forms.ModelForm):
    class Meta():
        model = Author
        fields = ["name", "age"]
        labels = {
            "name": "Name",
            "age": "Age"
        }


class BookForm(forms.ModelForm):
    class Meta():
        model = Book
        fields = ["title", "description", "category", "authors"]
        labels = {
            "title": "Title",
            "description": " Description",
            "category": "Category",
            "authors": "Authors"
        }


class RatingsForm(forms.ModelForm):
    class Meta():
        model = Rating
        fields = ["book", "rating"]
        labels = {
            "book": "Book",
            "rating": "Rating"
        }