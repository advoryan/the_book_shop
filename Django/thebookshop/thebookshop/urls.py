"""thebookshop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from data.views import *
from books.views import *

# from django.shortcuts import render - старая схема!"!!"
# def test_view(request):#test 
#     context = {}
#     return render(request, "test.html", context) # надо создать test.html !!!!!!

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('data/series/<int:pk>', SeriesDetail.as_view()), # PATH CONVERTER <int:year> - сппециальный ффромированый паттерн. Ждем число интеджер и используем для значения PK
    # 127.0.0.1:8000/data/series/4 - 4й pk - это что отразить, теперь надо как отобразить (дефолтный или другой)
    # надо изменить дефолтный шаблон
    # path('data/series/<int:pk>/<int:vasia>', SeriesDetail.as_view(), name='series-detail-view'),

    path('data/series/<int:pk>', SeriesDetail.as_view(), name='series-detail-view'),
    path('data/series/', SeriesView.as_view(), name='series-list-view'),
    path('data/series/create', SeriesCreateView.as_view(), name='series-create-view'),
    
    path('books/<int:pk>', BooksDetail.as_view(), name='books-detail-view'),
    path('books/', BooksView.as_view(), name='books-list-view'), 

    path('data/author/<int:pk>', AuthorDetail.as_view(), name='author-detail-view'),
    path('data/author/', AuthorView.as_view(), name='author-list-view'),
    path('data/author/create', AuthorCreateView.as_view(), name='author-create-view'),

    path('data/genre/<int:pk>', GenreDetail.as_view(), name='genre-detail-view'),
    path('data/genre/', GenreView.as_view(), name='genre-list-view'),
    path('data/genre/create', GenreCreateView.as_view(), name='genre-create-view'),

    path('data/publish/<int:pk>', PublishDetail.as_view(), name='publish-detail-view'),
    path('data/publish/', PublishView.as_view(), name='publish-list-view'),
    path('data/publish/create', PublishCreateView.as_view(), name='publish-create-view'),

    path('data/binding/<int:pk>', BindingDetail.as_view(), name='binding-detail-view'),
    path('data/binding/', BindingView.as_view(), name='binding-list-view'),
    path('data/binding/create', BindingCreateView.as_view(), name='binding-create-view'),

    path('data/format/<int:pk>', BookFormatDetail.as_view(), name='bookformat-detail-view'),
    path('data/format/', BookFormatView.as_view(), name='bookformat-list-view'),
    path('data/format/create', BindingCreateView.as_view(), name='bookformat-create-view'),

    path('', DictView.as_view(), name='dict_list')

]

