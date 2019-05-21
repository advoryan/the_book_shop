from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView, CreateView
from django.db.models import Q
from django.urls import reverse_lazy
from books.models import Book
from cart.models import BookInCart, Cart


class AddBookToChartView(UpdateView):
    template_name = "cart/add-product.html"
    model = BookInCart
    fields = ['quantity']

    def get_success_url(self):
        return self.request.POST.get("next", "")

    def get_object(self, queryset=None):
        print(self.request.user)
        cart_id = self.request.session.get('cart_id')

        if self.request.user.is_anonymous:
            user = None
        else:
            user = self.request.user

        cart, created = Cart.objects.get_or_create(pk=cart_id, defaults={'user': self.request.user}) #sdfdsdsfsdf
        self.request.session['cart_id'] = cart.pk
        book_pk = self.kwargs.get('pk')
        book = Book.objects.get(pk=book_pk)
        book_in_cart, created = self.model.objects.get_or_create(cart=cart, book=book, defaults={'quantity': 1})
        if not created:
            book_in_cart.quantity += 1
        return book_in_cart
        
    def get_context_data(self, **kwargs):
        content = super().get_context_data(*kwargs)
        content["book_id"] = self.kwargs.get("pk")
        content["next"] = self.kwargs.get("next", "/")   
        return content

    def get_success_url(self):
        return self.request.POST.get('next', '/')


class CartView(DetailView):
    model = Cart
    template_name = 'cart/view-cart.html'

    def get_object(self, queryset=None):
        cart_id = self.request.session.get('cart_id')
        if self.request.user.is_anonymous:
            user = None
        else:
            user = self.request.user
        cart, created = Cart.objects.get_or_create(pk=cart_id, defaults={'user': user})
        return cart

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        checkout_form = CheckOutOrderForm()
        checkout_form.fields['cart'].initial = self.object
        checkout_form.fields['status'].initial = new_order_status
        context['form'] = checkout_form
        print(context)
        return context
