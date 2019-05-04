from django.urls import path
from django.urls import include, path
from data.views import *
from books.views import *
from django.conf.urls.static import static

urlpatterns = [
    # path('', views.index, name='index'),

    path('<int:pk>', BookDetailView.as_view(), name='book-detail-view'),
    path('', BookListView.as_view(), name='book-list-view'), 
    path('create', BookCreateView.as_view(), name='book-create-view')
]

    # path('books/<int:pk>', BookDetailView.as_view(), name='book-detail-view'),
    # path('books/', BookListView.as_view(), name='book-list-view'), 
    # path('books/create', BookCreateView.as_view(), name='book-create-view')