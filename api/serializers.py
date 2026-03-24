from bookstore.models import Author, Book, Rating
from rest_framework import serializers


class RatingsSerializer(serializers.HyperlinkedModelSerializer):
    book = serializers.HyperlinkedRelatedField(
        view_name="book-detail", format="html", read_only=True
    )
    class Meta:
        model = Rating
        fields = ["rating", "book"]
        

class BookSerializer(serializers.HyperlinkedModelSerializer):
    authors = serializers.HyperlinkedRelatedField(
        view_name="author-detail", format="html", many=True, read_only=True
        )
    ratings = RatingsSerializer(many=True, read_only=True)
    
    class Meta:
        model = Book
        fields = ["url","title", "description", "category", "authors", "ratings"]


class AuthorSerializer(serializers.HyperlinkedModelSerializer):
    books = serializers.HyperlinkedRelatedField(view_name="book-detail", format="html", many=True, read_only=True)
    class Meta:
        model = Author 
        fields = ["url", "name", "age", "books"]
