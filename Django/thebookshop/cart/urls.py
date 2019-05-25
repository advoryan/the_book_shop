from django.urls import path
from cart.views import AddBookToChartView, CartView

urlpatterns = [
    path('add-to-cart/<int:pk>', AddBookToChartView.as_view(), name='add-to-cart'),
    path('view-cart/', CartView.as_view(), name='view-cart'),
    # path('delete-from-cart/<int:pk>', DeleteBookFromCart.as_view(), name='delete-from-cart')
]