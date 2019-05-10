from django.urls import path
from data.views import *

urlpatterns = [

    path('data/series/<int:pk>', SeriesDetail.as_view(), name='series-detail-view'),
    path('data/series/', SeriesView.as_view(), name='series-list-view'),
    path('data/series/create', SeriesCreateView.as_view(), name='series-create-view'),
    path('data/series/<int:pk>/update', SeriesUpdateView.as_view(), name='series-update-view'),
    path('data/series/<int:pk>/delete', SeriesDeleteView.as_view(), name='series-delete-view'),

    path('data/author/<int:pk>', AuthorDetail.as_view(), name='author-detail-view'),
    path('data/author/', AuthorView.as_view(), name='author-list-view'),
    path('data/author/create', AuthorCreateView.as_view(), name='author-create-view'),
    path('data/author/<int:pk>/update', AuthorUpdateView.as_view(), name='author-update-view'),
    path('data/author/<int:pk>/delete', AuthorDeleteView.as_view(), name='author-delete-view'),

    path('data/genre/<int:pk>', GenreDetail.as_view(), name='genre-detail-view'),
    path('data/genre/', GenreView.as_view(), name='genre-list-view'),
    path('data/genre/create', GenreCreateView.as_view(), name='genre-create-view'),
    path('data/genre/<int:pk>/update', GenreUpdateView.as_view(), name='genre-update-view'),
    path('data/genre/<int:pk>/delete', GenreDeleteView.as_view(), name='genre-delete-view'),

    path('data/publish/<int:pk>', PublishDetail.as_view(), name='publish-detail-view'),
    path('data/publish/', PublishView.as_view(), name='publish-list-view'),
    path('data/publish/create', PublishCreateView.as_view(), name='publish-create-view'),
    path('data/publish/<int:pk>/update', PublishUpdateView.as_view(), name='publish-update-view'),
    path('data/publish/<int:pk>/delete', PublishDeleteView.as_view(), name='publish-delete-view'),

    path('data/binding/<int:pk>', BindingDetail.as_view(), name='binding-detail-view'),
    path('data/binding/', BindingView.as_view(), name='binding-list-view'),
    path('data/binding/create', BindingCreateView.as_view(), name='binding-create-view'),
    path('data/binding/<int:pk>/update', BindingUpdateView.as_view(), name='binding-update-view'),
    path('data/binding/<int:pk>/delete', BindingDeleteView.as_view(), name='binding-delete-view'),

    path('data/format/<int:pk>', BookFormatDetail.as_view(), name='bookformat-detail-view'),
    path('data/format/', BookFormatView.as_view(), name='bookformat-list-view'),
    path('data/format/create', BookFormatView.as_view(), name='bookformat-create-view'),
    path('data/format/<int:pk>/update', BookFormatUpdateView.as_view(), name='bookformat-update-view'),
    path('data/format/<int:pk>/delete',  BookFormatDeleteView.as_view(), name='bookformat-delete-view'),
]