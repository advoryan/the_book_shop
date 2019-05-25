from django import forms
from django.forms import ModelForm
from .models import BookInCart

class AddBookForm(ModelForm):
    class Meta:
        model = BookInCart
        fields = ["cart", "book", "quantity"]
        widgets = { "cart": forms.HiddenInput(),"book": forms.HiddenInput()}
