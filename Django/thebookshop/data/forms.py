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
        fields = '__all__'

class AuthorCreateForm(ModelForm):
    class Meta:
        model = Author
        fields = '__all__'

class GenreCreateForm(ModelForm):
    class Meta:
        model = Genre
        fields = '__all__'

class PublishCreateForm(ModelForm):
    class Meta:
        model = Publish
        fields = '__all__'

class BindingCreateForm(ModelForm):
    class Meta:
        model = Binding
        fields = '__all__'

class BookFormatCreateForm(ModelForm):
    class Meta:
        model = BookFormat
        fields = '__all__'
