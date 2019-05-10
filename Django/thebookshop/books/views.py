from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.edit import DeleteView
from books.models import Book
from books.forms import BookCreateForm
from django.urls import reverse_lazy

class BookDetailView(DetailView):
    model = Book

class BookListView(ListView):
    model = Book

class BookCreateView(CreateView):
    model = Book
    template_name = 'data/Creation_form.html'
    form_class = BookCreateForm
    def get_success_url(self):
        detail1 = self.request.POST.get("detail")
        list1 = self.request.POST.get("list")
        view1 = self.request.POST.get("view")
        if detail1:
            return reverse_lazy("book-detail-view", kwargs={"pk": self.object.pk})
        elif list1:
            return reverse_lazy("book-list-view")
        return reverse_lazy("book-create-view")

class BookUpdateView(UpdateView):
    model = Book
    form_class = BookCreateForm
    template_name = "data/Delete_form.html"

class BookDeleteView(DeleteView):
    success_url = reverse_lazy("book-list-view")
    model = Book