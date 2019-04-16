from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from .models import *

class SeriesDetail(DetailView):
    model = Series
    # # template_name = - изменить тип шаблона
    # abc = 2 * 2
    # # переопределение методов родителя get_context_data
    # def get_context_data(self, **kwargs): # переопределяем функцию папашки
    #     context = super().get_context_data(**kwargs) # проим отработать отцовский метод с помощью super
    #     context["ffff"] = self.abc
    #     return context

class AuthorDetail(DetailView):
    model = Author

class GenreDetail(DetailView):
    model = Genre

class PublishDetail(DetailView):
    model = Publish

class BindingDetail(DetailView):
    model = Binding

class BookFormatDetail(DetailView):
    model = BookFormat

    


