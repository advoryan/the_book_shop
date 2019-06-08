from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.edit import DeleteView
from books.models import Book
from books.forms import BookCreateForm, SearchForm, BookUpdateForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import PermissionRequiredMixin

class BookDetailView(DetailView):
    model = Book

class BookListView(ListView):
    model = Book
    def get_queryset(self):
        qs = super().get_queryset()
        search = self.request.GET.get("search", 0)
        if search != 0:
            return qs.filter(name__icontains=search)
        return qs
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        f = SearchForm()
        context["form"] = f       
        return context

class BookCreateView(PermissionRequiredMixin, CreateView):
    model = Book
    template_name = 'data/Creation_form.html'
    form_class = BookCreateForm
    permission_required = 'books.edit'

    def get_success_url(self):
        detail1 = self.request.POST.get("detail")
        list1 = self.request.POST.get("list")
        view1 = self.request.POST.get("view")
        if detail1:
            return reverse_lazy("book-detail-view", kwargs={"pk": self.object.pk})
        elif list1:
            return reverse_lazy("book-list-view")
        return reverse_lazy("book-create-view")

class BookUpdateView(PermissionRequiredMixin, UpdateView):
    model = Book
    form_class = BookUpdateForm
    template_name = "books/book_update.html"
    permission_required = 'books.edit'

    def get_success_url(self):
        if self.request.POST.get('detail'):
            return reverse_lazy('book-detail-view', kwargs={'pk': self.object.pk})
        return reverse_lazy('book-list-view')

class BookDeleteView(PermissionRequiredMixin, DeleteView):
    success_url = reverse_lazy("book-list-view")
    template_name = 'books/book_delete.html'
    model = Book
    permission_required = 'books.edit'
