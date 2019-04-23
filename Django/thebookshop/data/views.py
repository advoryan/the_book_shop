from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.base import TemplateView
# from django.views.generic.edit import CreateView
from .models import *
from books.views import *
from books.models import *
from .forms import *


# class Searching(ListView):
#     def get_queryset(self):
#         qs = super().get_queryset()
#         search = self.request.GET.get("search", 0)
#         if search != 0:
#             return qs.filter(pk__gte=search)
#         return qs
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         f = SearchForm()
#         context["form"] = f       
#         # context["form"] = f
#         return context


class SeriesDetail(DetailView):
    model = Series
    # template_name = - изменить тип шаблона
    abc = 2 * 2
    # переопределение методов родителя get_context_data
    def get_context_data(self, **kwargs): # переопределяем функцию папашки
        context = super().get_context_data(**kwargs) # проим отработать отцовский метод с помощью super
        print(self, kwargs) # - 
        # context["ffff"] = self.abc
        return context

class SeriesView(ListView):
    model = Series
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

# class SeriesCreateView(CreateView):
#     pass

    # template_name = "data/series_list.html"
    # def get_queryset(self):
    #     queryset = ["fgsdg", "sdfgsdfg", "gfdgs"]
    

    #    model = Series
    # def get_queryset(self):
    #     return ["2"]

    # def get_queryset(self):
    #     a = self.model
    #     return a.objects.filter(pk__gt=25)

    # def get_queryset(self):
    #     return Series.objects.filter(pk__gt=25)
   
# class SeriesView(ListView):
#     model = Series
#     queryset = Series.objects.filter(pk__gt=20)   # работает
   
    # def get_context_data(self, **kwargs): # переопределяем функцию папашки
    #         context = super().get_context_data(**kwargs) # проим отработать отцовский метод с помощью super
    #         print(context) # - 
    #         a = context["object_list"]# context["ffff"] = self.abc
    #         b = a.filter(pk__gt=50) # фильтр пк > 50
    #         context["object_list"] = b
    #         return context


    # def get_queryset(self):
    #     return Series.objects.filter(description__icontains='desk')[:5] # - it's work!!!
    # model = Series
    # # template_name = - изменить тип шаблона
    # abc = 2 * 2
    # # переопределение методов родителя get_context_data
    # def get_context_data(self, **kwargs): # переопределяем функцию папашки
    #     context = super().get_context_data(**kwargs) # проим отработать отцовский метод с помощью super
    #     print(self, kwargs) # - 
    #     # context["ffff"] = self.abc
    #     return context

class BooksView(ListView):
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

class BooksDetail(DetailView):
    model = Book

class AuthorDetail(DetailView):
    model = Author

class AuthorView(ListView):
    model = Author
    def get_queryset(self):
        qs = super().get_queryset()
        search = self.request.GET.get("search", 0)
        if search != 0:
            return qs.filter(last_name__icontains=search)
        return qs
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        f = SearchForm()
        context["form"] = f       
        return context

        # return qs.filter(first_name=form1)

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     f = SearchForm()
    #     context["form"] = f
    #     return context

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

class DictView(TemplateView):
    template_name = "data/Dict_List.html"

