from ..models import Book, Author, Rating
from django.db.models import CharField, Max, Min, Avg, Count, Sum, Value
from django.db import connection
from pprint import pprint
from django.db.models.functions import Length, Concat

def run():
    # print("starting the ORM script....\n")
    # print("Starting with .all()\n")
    # authors = Author.objects.all()
    # books = Book.objects.all()
    # ratings = Rating.objects.all()
   
    # print("Authors: ")
    # print(authors)
    # print("\n")
    # print("Books:")
    # print(books)
    # print("\n")
    # print("Ratings:")
    # print(ratings)
    # print("\n")
    # print("\nNext we have filter() for each Model\n")

    # authors = Author.objects.filter(name__contains="R")
    # books = Book.objects.filter(title__exact="Frankenstein")
    # ratings = Rating.objects.filter(rating__gte=3).order_by("-rating")

    # print("Authors with name containing 'R': ")
    # print(authors)
    # print("\n")
    # print("Books where title Exactly matches: ")
    # print(books)
    # print("\n")
    # print("Ratings where rating is greater than or equal to 3: ")
    # print(ratings)
    # print("\n")
    # print("\n next use some aggregations...\n")

    # authors = Author.objects.aggregate(age=Max("age"))
    # books = Book.objects.aggregate(rating=Avg("ratings__rating"))
    # ratings = Rating.objects.aggregate(rating=Min("rating"))
    # ratings_all = Rating.objects.aggregate(
    #     avg=Avg("rating"),
    #     max=Max("rating"),
    #     min=Min("rating"), 
    #     count=Count("rating"), 
    #     sum=Sum("rating")
    #     )

    # print("Authors Max age: ")
    # print(authors)
    # print("\n")
    # print("Books Avg rating for a book:")
    # print(books)
    # print("\n")
    # print("Ratings min rating given:")
    # print(ratings)
    # print("\n")
    # print("All Ratings aggregations:")
    # print(ratings_all)
    # print("\n")


    # book = Book.objects.first()

    # print(book.ratings.all())


    # # fetch all books and apply annotate on the length of the title

    # books = Book.objects.annotate(len_title=Length("title")).filter(
    #     len_title__lte=30
    # ).order_by("len_title")

    # print(books.values("title", "len_title")) 
    # print("\n")

    # # add a concatenated message to a model

    # concat = Concat("title", Value(": Avg Rating -> "), Avg("ratings__rating"), output_field=CharField())

    # books = Book.objects.annotate(message=concat)

    # for b in books:
    #     print(b.message)
    # print("\n")

    # print([b.message for b in books])
    

    """
        Methods for solving the N+1 problem to optimise the queries and prefetch data and related
    """

    books = Book.objects.prefetch_related('ratings', 'authors')

    for b in books:
        print(f"-------{b.title}-------")
        for a in b.authors.all():
            print(f"Author: {a.name}")

        for r in b.ratings.all():
            print(f"Rating: {r.rating}")


    rating = Rating.objects.only("rating", "book__title").select_related("book")

    for r in rating:
        print(f"{r.book.title} was rated {r.rating}")

    pprint(connection.queries)