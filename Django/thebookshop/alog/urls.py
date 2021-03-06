from django.urls import path
from alog.views import *

urlpatterns = [
    path('login', LoginView.as_view(), name='log-in'),
    path('logout', LogoutView.as_view(), name='log-out'),
    path('create-user', CreateUser.as_view(), name='create-user'),
    path('update-user/<int:pk>', UpdateUser.as_view(), name='update-user'),
    path('view-user/<int:pk>', ViewUser.as_view(), name='view-user'),
    path('change-password', PasswordChangeView.as_view(), name='change-password'),
    path('change-password-done', PasswordChangeDone.as_view(), name='change-password-done'),
]