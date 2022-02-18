from dataclasses import fields
from os import name
from pyexpat import model
from .models import Contact
from django.forms import ModelForm


class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'