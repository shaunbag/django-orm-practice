from django.shortcuts import render
from bookstore.models import Book, Author, Rating
from rest_framework import status, renderers
from rest_framework.response import Response
from .serializers import BookSerializer, AuthorSerializer, RatingsSerializer
from rest_framework.decorators import api_view, action
from rest_framework import viewsets
from rest_framework.reverse import reverse 
from rest_framework import permissions

@api_view(["GET"])
def api_root(request):
    return Response(
        {
            "books": reverse("book-view", request=request, format=None),
            "authors": reverse("author-view", request=request, format=None),
            "ratings": reverse("rating-view", request=request, format=None)
        }
    )


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

    @action(detail=True, renderer_classes=[renderers.StaticHTMLRenderer])
    def books(self, request, *args, **kwargs):
        return Response(self.books)
    

    def perform_create(self, serializer):
        return super().perform_create(serializer)


class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [permissions.IsAuthenticated]

    @action(detail=True, renderer_classes=[renderers.StaticHTMLRenderer])
    def authors(self, request, *args,**kwargs):
        return Response(self.authors)
    
    def perform_create(self, serializer):
        return super().perform_create(serializer)


class RatingsViewSet(viewsets.ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingsSerializer
    permission_classes = [permissions.IsAuthenticated]

    @action(detail=True, renderer_classes=[renderers.StaticHTMLRenderer])
    def ratings(self, request, *args, **kwargs):
        return Response(self.ratings)
    

    def perform_create(self, serializer):
        return super().perform_create(serializer)