from cProfile import label
from pyexpat import model
from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length= 100)
    message = models.TextField(max_length=300)
    email = models.EmailField()
    phone = models.CharField(blank=True, null=True, max_length=10)
    attachment = models.ImageField(upload_to='images/', blank=True, null=True)

    def __str__(self) :
        return self.name