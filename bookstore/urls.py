from django.urls import path
from . import views

urlpatterns = [
    path("author/", views.author, name="author"),
    path("add_author", views.add_author, name="add-author"),
    path("book/", views.book, name="book"),
    path("add_book", views.add_book, name="add-book"),
    path("ratings/", views.rating, name="ratings"),
    path("add_rating", views.add_rating, name="add-rating")
]
