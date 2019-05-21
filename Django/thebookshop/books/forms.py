from django import forms
from django.forms import ModelForm
from books.models import Book

class SearchForm(forms.Form):
    search = forms.CharField(label="Поиск")
    
class BookCreateForm(ModelForm):
    class Meta:
        model = Book
        fields = '__all__'