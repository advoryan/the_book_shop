from django.urls import path
from books.views import *

urlpatterns = [
    path('list', BookListView.as_view(), name='book-list-view'),    
    path('<int:pk>', BookDetailView.as_view(), name='book-detail-view'),
    path('create', BookCreateView.as_view(), name='book-create-view'),
    path('<int:pk>/update', BookUpdateView.as_view(), name='book-update-view'),
    path('<int:pk>/delete', BookDeleteView.as_view(), name='book-delete-view'),
]