from django import forms
from django.forms import ModelForm
from data.models import *
# форма для поиска

class SearchForm(forms.Form):
    search = forms.CharField(label="Поиск")
    # active = forms.BooleanField(label="Активный", required=False)
    # search = forms.CharField(label="Поиск", required=True)

# Модельная форма
class SeriesCreateForm(ModelForm):
    class Meta:
        model = Series
        fields = ('name', 'description') # без active

class AuthorCreateForm(ModelForm):
    class Meta:
        model = Author
        fields = ('first_name', 'last_name', 'country')

class GenreCreateForm(ModelForm):
    class Meta:
        model = Genre
        fields = ('name',)

class PublishCreateForm(ModelForm):
    class Meta:
        model = Publish
        fields = ('name', 'country', 'city')

class BindingCreateForm(ModelForm):
    class Meta:
        model = Binding
        fields = ('binding_type',)

class BookFormatCreateForm(ModelForm):
    class Meta:
        model = BookFormat
        fields = ('size',)