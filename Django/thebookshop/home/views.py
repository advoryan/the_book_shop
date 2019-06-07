from django.shortcuts import render
from books.models import Book
from data.models import Author
from django.db.models import Q
from django.views.generic.list import ListView
from data.forms import *
# import operator
# from django.contrib.auth import views as auth_views
# from django.contrib.auth.views import LoginView, LogoutView
# from django.urls import reverse_lazy


# импорт библиотек !!!!!!!!!! + User ----- для аутентификации
# def home(request):
# 	result = []
# 	context ={"accounts": result}
# 	# user = User.objects.get(pk=2)
# 	# login(request, user)
# return  render (request, "home.html", context)


class HomeListView(ListView):
    model = Book
    template_name = 'home/home.html'
    # def get_queryset(self, **kwargs):
    #     qs = super().get_queryset(**kwargs)
    #     search = self.request.GET.get('name', 0)

    #     obj = Author.objects.filter(first_name__icontains=search)
    #     list_book_pk = []
    #     for aut in obj:
    #         for i in aut.books.all():
    #             list_book_pk.append(i.pk)
    #     if qs.filter(Q(name__icontains=search) | Q(pk__in=list_book_pk)).exists():
    #         return qs.filter(Q(name__icontains=search) | Q(pk__in=list_book_pk))
    #     return qs.order_by('-updated_date')[0:3]

    def get_queryset(self):
        qs = super().get_queryset()
        search = self.request.GET.get("search", 0)
        if search != 0:
            return qs.filter(Q(name__icontains=search) | Q(author__last_name__icontains=search)).distinct()
        return qs.order_by('-updated_date')[0:3]
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        f = SearchForm()
        context["form"] = f
        return context

# class LogInView(LoginView):
#     template_name = 'home/login.html'

# class LogOutView(LogoutView):
#     extra_context = 'none'