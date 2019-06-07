from django.urls import path, include
from home.views import HomeListView#, LogInView, LogOutView

urlpatterns = [
    path('', HomeListView.as_view(), name='home-list-view'),
    # path('login', LogInView.as_view(), name='log-in'),
    # path('logout', LogOutView.as_view(), name='log-out'),
    # path('accounts/', include('django.contrib.auth.urls'))
]