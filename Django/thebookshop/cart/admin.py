from django.contrib import admin
from .models import BookInCart, Cart

class CartAdmin(admin.ModelAdmin):
    list_display = ['user', 'created_day', 'updated_date'] # указанные поля
    # list_filter = ("name", 'author', 'serie', 'genre')  # отфильтровать по полям
    # search_fields = [field.name for field in Book._meta.fields]  # поиск по всем полям

    class Meta:
        model = Cart

admin.site.register(Cart)
admin.site.register(BookInCart)