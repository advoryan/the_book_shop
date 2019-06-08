from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView, CreateView
from django.views.generic import DeleteView
from django.db.models import Q
from django.urls import reverse_lazy
from books.models import Book
from cart.models import BookInCart, Cart, User
from .forms import AddBookForm 
from data.models import OrderStatus
from order.forms import CheckOutOrderForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import authenticate, login

new_order_status = OrderStatus.objects.get(pk=1)
# cart, created = OrderStatus.get_or_create(pk=1)

class AddBookToChartView(UpdateView):
    template_name = "cart/add-product.html"
    model = BookInCart
    form_class = AddBookForm

    def get_object(self, queryset=None):
        # print(self.request.user)
        cart_id = self.request.session.get('cart_id')

        if self.request.user.is_anonymous:
            user = None
        else:
            user = self.request.user

        # cart, created = Cart.objects.get_or_create(pk=cart_id, defaults={'user': self.request.user}) #sdfdsdsfsdf
        cart, created = Cart.objects.get_or_create(pk=cart_id, defaults={'user': user}) #sdfdsdsfsdf
        self.request.session['cart_id'] = cart.pk
        print(self.request.session['cart_id'])
        book_pk = self.kwargs.get('pk')
        book = Book.objects.get(pk=book_pk)
        book_in_cart, created = self.model.objects.get_or_create(cart=cart, book=book, defaults={'quantity': 1})
        if not created:
            book_in_cart.quantity += 1
        return book_in_cart
        
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['next'] = self.request.GET.get('next', '/')
        return context

    def get_success_url(self):
        if self.request.POST.get('back'):
            product = self.model.objects.get(pk=self.object.pk)
            if product.quantity > 1:
                product.quantity -= 1
                product.save()
            else:
                product.delete()
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

class CartUserList(ListView): #LoginRequiredMixin,
    model = Cart
    # template_name = 'cart/cart_user_list.html'
    template_name = 'cart/view-cart.html'
    # login_url = '/alog/login'

    # def get_queryset(self, **kwargs):
    #     qs = super().get_queryset(**kwargs)
    #     current_user = self.request.user
    #     return qs.filter(user=current_user)

class DeleteBookFromCart(DeleteView):
    model = BookInCart
    template_name = 'cart/delete-book.html'

    def get_success_url(self):
        return reverse_lazy('view-cart')

