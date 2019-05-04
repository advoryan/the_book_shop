from django import forms
from django.forms import ModelForm
from data.models import *
# ФОРМЫ КНИГИ

class SeriesCreateForm(ModelForm):
    class Meta:
        model = Book
        fields = ('name', 'image', 'description', 'price', 'author', 'rate') # без active
