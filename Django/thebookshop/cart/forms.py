from django import forms
from django.forms import ModelForm
from .models import BookInCart

class AddBookForm(form.Model):
    class Meta
        model = BookInCart
        fields = ["cart", "name", "quantity"]
        widgets = { "book": forms.HiddenInput(),}
