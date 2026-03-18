from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Author(models.Model):
    name = models.CharField(max_length=100)
    age = models.BigIntegerField()

    def __str__(self):
        return self.name


class Book(models.Model):
    class CategoryChoice(models.TextChoices):
        HORROR = "HORROR", " Horror"
        CLASSICAL = "CLASSICAL", "Classical"
        SCIFI = "SCIFI", "Sci-Fi"
        FANTASY = "FANTASY", "Fantasy"
        HISTORICAL = "HISTORICAL", "Historical"
        SCIENTIFIC = "SCIENTIFIC", "Scientific"

    title = models.CharField(max_length=100)
    description = models.TextField()
    category = models.CharField(choices=CategoryChoice, default=CategoryChoice.CLASSICAL)
    authors = models.ManyToManyField(Author, related_name="books")

    def __str__(self):
        return self.title


class Rating(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    rating = models.PositiveSmallIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])