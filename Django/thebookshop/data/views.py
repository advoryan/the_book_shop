from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.base import TemplateView
from .models import *
from books.views import *
from books.models import *

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

class BooksDetail(DetailView):
    model = Book

class AuthorDetail(DetailView):
    model = Author

class AuthorView(ListView):
    model = Author

class GenreDetail(DetailView):
    model = Genre

class GenreView(ListView):
    model = Genre

class PublishDetail(DetailView):
    model = Publish

class PublishView(ListView):
    model = Publish

class BindingDetail(DetailView):
    model = Binding

class BindingView(ListView):
    model = Binding

class BookFormatDetail(DetailView):
    model = BookFormat

class BookFormatView(ListView):
    model = BookFormat
class DictView(TemplateView):
    template_name = "data/Dict_List.html"

