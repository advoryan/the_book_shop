from django.urls import include, path
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from cart.views import *

admin.autodiscover()

urlpatterns = [
    path('admin/', admin.site.urls),
    path('books/', include('books.urls')),
    path('data/', include('data.urls')),
    path('cart/', include('cart.urls')),
    path('order/', include('order.urls')),
    path('alog/', include('alog.urls')),
    path('', include('home.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)