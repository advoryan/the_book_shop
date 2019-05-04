from django.shortcuts import render
from django.views.generic.list import ListView
from .models import *
from data.forms import *
from data.views import *

# Create your views here.

class BookListView(ListView):
    model = Book

class BookDetailView(ListView):
    model = Book

class BookCreateView(ListView):
    model = Book
    form_class = SeriesCreateForm
    def get_success_url():
        return reverse_lazy("book-detail-views", kwargs={"pk": self.object.pk})