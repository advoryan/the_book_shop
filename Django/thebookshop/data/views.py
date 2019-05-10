from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.edit import DeleteView
from .models import *
from books.views import *
from books.models import *
from .forms import *
from django.db.models import Q
from django.urls import reverse_lazy

class SeriesDetail(DetailView):
    model = Series
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print(self, kwargs)
        return context

class SeriesView(ListView):
    model = Series
    def get_queryset(self):
        qs = super().get_queryset()
        # active = self.request.GET.get("on", False)
        search = self.request.GET.get("search", 0)
        if search != 0:
            return qs.filter(name__icontains=search)
        return qs
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        f = SearchForm()
        context["form"] = f       
        return context

class SeriesCreateView(CreateView):
    model = Series
    template_name = 'data/Creation_form.html'
    form_class = SeriesCreateForm
    def get_success_url(self):
        # new_url = super().get_success_url() - не обязательно надо, пользуемся родителем
        detail1 = self.request.POST.get("detail")
        list1 = self.request.POST.get("list")
        view1 = self.request.POST.get("view")
        if detail1:
            return reverse_lazy("series-detail-view", kwargs={"pk": self.object.pk})
        elif list1:
            return reverse_lazy("series-list-view")
        return reverse_lazy("series-create-view")

class SeriesUpdateView(UpdateView):
    model = Series
    template_name = 'data/Update_form.html'
    form_class = SeriesCreateForm
    def get_success_url(self):
        if self.request.POST.get('detail'):
            return reverse_lazy('series-detail-view', kwargs={'pk': self.object.pk})
        return reverse_lazy('series-list-view')

class SeriesDeleteView(DeleteView):
    success_url = reverse_lazy("series-list-view")
    model = Series
    template_name = "data/Delete_form.html"


class AuthorDetail(DetailView):
    model = Author

class AuthorView(ListView):
    model = Author
    def get_queryset(self):
        qs = super().get_queryset()
        search = self.request.GET.get("search", 0) # СЛОВАРЬ - self.request.GET
        if search != 0:
            return qs.filter(last_name__icontains=search)
        return qs
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        f = SearchForm()
        context["form"] = f       
        return context

class AuthorCreateView(CreateView):
    model = Series
    template_name = 'data/Creation_form.html'
    form_class = AuthorCreateForm
    def get_success_url(self):
        detail1 = self.request.POST.get("detail")
        list1 = self.request.POST.get("list")
        view1 = self.request.POST.get("view")
        if detail1:
            return reverse_lazy("author-detail-view", kwargs={"pk": self.object.pk})
        elif list1:
            return reverse_lazy("author-list-view")
        return reverse_lazy("author-create-view")

class AuthorUpdateView(UpdateView):
    model = Author
    template_name = 'data/Update_form.html'
    form_class = AuthorCreateForm
    def get_success_url(self):
        if self.request.POST.get('detail'):
            return reverse_lazy('author-detail-view', kwargs={'pk': self.object.pk})
        return reverse_lazy('author-list-view')

class AuthorDeleteView(DeleteView):
    success_url = reverse_lazy("author-list-view")
    model = Author
    template_name = "data/Delete_form.html"


class GenreDetail(DetailView):
    model = Genre

class GenreView(ListView):
    model = Genre
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

class GenreCreateView(CreateView):
    model = Series
    template_name = 'data/Creation_form.html'
    form_class = GenreCreateForm
    def get_success_url(self):
        detail1 = self.request.POST.get("detail")
        list1 = self.request.POST.get("list")
        view1 = self.request.POST.get("view")
        if detail1:
            return reverse_lazy("genre-detail-view", kwargs={"pk": self.object.pk})
        elif list1:
            return reverse_lazy("genre-list-view")
        return reverse_lazy("genre-create-view")

class GenreUpdateView(UpdateView):
    model = Genre
    template_name = 'data/Update_form.html'
    form_class = GenreCreateForm
    def get_success_url(self):
        if self.request.POST.get('detail'):
            return reverse_lazy('genre-detail-view', kwargs={'pk': self.object.pk})
        return reverse_lazy('genre-list-view')

class GenreDeleteView(DeleteView):
    success_url = reverse_lazy("genre-list-view")
    model = Genre
    template_name = "data/Delete_form.html"


class PublishDetail(DetailView):
    model = Publish

class PublishView(ListView):
    model = Publish
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

class PublishCreateView(CreateView):
    model = Series
    template_name = 'data/Creation_form.html'
    form_class = PublishCreateForm
    def get_success_url(self):
        detail1 = self.request.POST.get("detail")
        list1 = self.request.POST.get("list")
        view1 = self.request.POST.get("view")
        if detail1:
            return reverse_lazy("publish-detail-view", kwargs={"pk": self.object.pk})
        elif list1:
            return reverse_lazy("publish-list-view")
        return reverse_lazy("publish-create-view")

class PublishUpdateView(UpdateView):
    model = Publish
    template_name = 'data/Update_form.html'
    form_class = PublishCreateForm
    def get_success_url(self):
        if self.request.POST.get('detail'):
            return reverse_lazy('publish-detail-view', kwargs={'pk': self.object.pk})
        return reverse_lazy('publish-list-view')

class PublishDeleteView(DeleteView):
    success_url = reverse_lazy("publish-list-view")
    model = Publish
    template_name = "data/Delete_form.html"


class BindingDetail(DetailView):
    model = Binding

class BindingView(ListView):
    model = Binding
    def get_queryset(self):
        qs = super().get_queryset()
        search = self.request.GET.get("search", 0)
        if search != 0:
            return qs.filter(binding_type__icontains=search)
        return qs
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        f = SearchForm()
        context["form"] = f       
        return context

class BindingCreateView(CreateView):
    model = Series
    template_name = 'data/Creation_form.html'
    form_class = BindingCreateForm
    def get_success_url(self):
        # new_url = super().get_success_url() - не обязательно надо, пользуемся родителем
        detail1 = self.request.POST.get("detail")
        list1 = self.request.POST.get("list")
        view1 = self.request.POST.get("view")
        if detail1:
            return reverse_lazy("binding-detail-view", kwargs={"pk": self.object.pk})
        elif list1:
            return reverse_lazy("binding-list-view")
        return reverse_lazy("binding-create-view")

class BindingUpdateView(UpdateView):
    model = Binding
    template_name = 'data/Update_form.html'
    form_class = BindingCreateForm
    def get_success_url(self):
        if self.request.POST.get('detail'):
            return reverse_lazy('binding-detail-view', kwargs={'pk': self.object.pk})
        return reverse_lazy('binding-list-view')

class BindingDeleteView(DeleteView):
    success_url = reverse_lazy("binding-list-view")
    model = Binding
    template_name = "data/Delete_form.html"
 

class BookFormatDetail(DetailView):
    model = BookFormat

class BookFormatView(ListView):
    model = BookFormat
    def get_queryset(self):
        qs = super().get_queryset()
        search = self.request.GET.get("search", 0)
        if search != 0:
            return qs.filter(size__icontains=search)
        return qs
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        f = SearchForm()
        context["form"] = f       
        return context

class BookFormatCreateView(CreateView):
    model = Series
    template_name = 'data/Creation_form.html'
    form_class = BookFormatCreateForm
    def get_success_url(self):
        # new_url = super().get_success_url() - не обязательно надо, пользуемся родителем
        detail1 = self.request.POST.get("detail")
        list1 = self.request.POST.get("list")
        view1 = self.request.POST.get("view")
        if detail1:
            return reverse_lazy("bookformat-detail-view", kwargs={"pk": self.object.pk})
        elif list1:
            return reverse_lazy("bookformat-list-view")
        return reverse_lazy("bookformat-create-view")

class BookFormatUpdateView(UpdateView):
    model = BookFormat
    template_name = 'data/Update_form.html'
    form_class = BookFormatCreateForm
    def get_success_url(self):
        if self.request.POST.get('detail'):
            return reverse_lazy('bookformat-detail-view', kwargs={'pk': self.object.pk})
        return reverse_lazy('bookformat-list-view')

class BookFormatDeleteView(DeleteView):
    success_url = reverse_lazy("bookformat-list-view")
    model = BookFormat
    template_name = "data/Delete_form.html"



class DictView(TemplateView):
    template_name = "data/Dict_List.html"

