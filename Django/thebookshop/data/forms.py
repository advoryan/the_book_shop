from django import forms
# форма для поиска

class SearchForm(forms.Form):
    search = forms.CharField(label="Поиск") #, required=True
    # search = forms.CharField(label="Поиск", required=True)v