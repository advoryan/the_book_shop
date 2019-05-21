from django.urls import path
from cart.views import AddBookToChartView

urlpatterns = [
    path('<int:pk>', AddBookToChartView.as_view(), name='add-to-cart'),
]