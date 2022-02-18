from cProfile import label
from pyexpat import model
from tkinter import Label
from django.db import models
from author.models import Author

# Create your models here.
class Article(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=30)
    body = models.TextField(max_length=100)
    created_at = models.DateTimeField(auto_now=True, )
    updated_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.name


