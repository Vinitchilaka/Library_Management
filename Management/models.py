from django.db import models

class Book(models.Model):
    book_name = models.CharField(max_length=100)
    book_author = models.CharField(max_length=75)
    book_isbn = models.PositiveIntegerField(unique=True)
    book_category = models.CharField(max_length=100)
    class Meta:
        db_table  = "Books_Master"

    def __str__(self):
        return f'''{self.__dict__}'''
    def __repr__(self):
        return str(self)

