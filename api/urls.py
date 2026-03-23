from django.urls import path
from . import views

urlpatterns = [
    path("", views.api_root, name="api-root"),
    path("books/", views.BookViewSet.as_view({"get": "list", "post": "create"}), name="book-view"),
    path("book/<int:pk>", views.BookViewSet.as_view({"get": "retrieve"}), name="book-detail"),
    path("author/", views.AuthorViewSet.as_view({"get": "list", "post": "create"}), name="author-view"),
    path("author/<int:pk>", views.AuthorViewSet.as_view({"get": "retrieve"}), name="author-detail"),
    path("rating/", views.RatingsViewSet.as_view({"get": "list", "post": "create"}), name="rating-view"),
    path("rating/<int:pk>", views.RatingsViewSet.as_view({"get": "retrieve"}), name="rating-detail")
]
