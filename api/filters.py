import django_filters
from bookstore.models import Book, Author, Rating


class BookFilter(django_filters.FilterSet):
    class Meta:
        model = Book
        fields = {
                'category' : ['exact'],
            }
        

class AuthorFilter(django_filters.FilterSet):
    class Meta:
        model = Author
        fields = {
            'age':['lt', 'gt', 'range']
        }


class RatingFilter(django_filters.FilterSet):
    class Meta:
        model = Rating
        fields = {
            'rating': ['gt', 'lt', 'range'],
        }