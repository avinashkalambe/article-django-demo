from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.
class Author(models.Model):

    # name = models.CharField(max_length=50)
    # email = models.EmailField()
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    profile_pic = models.ImageField(upload_to='profile_pic/', blank= True, null=True)
    
    def __str__(self):
        return self.user.username

    def get_absolute_url(self):
        return reverse('create_author')