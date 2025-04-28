from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    description = models.TextField()
    published_year = models.IntegerField()

    def __str__(self):
        return self.title

class Review(models.Model):
    content = models.TextField()
    book = models.ForeignKey(Book, on_delete=models.CASCADE)

    def __str__(self):
        return f"Review for {self.book.title}"


class Genre(models.Model):
    name = models.CharField(max_length=50)
    books = models.ManyToManyField(Book)

    def __str__(self):
        return self.name
