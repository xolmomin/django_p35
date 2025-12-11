from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, DetailView, TemplateView

from apps.models import Product, User


class ProductListView(ListView):
    queryset = Product.objects.all()
    template_name = 'apps/product-list.html'
    context_object_name = 'products'
    paginate_by = 3


class ProductDetailView(DetailView):
    queryset = Product.objects.all()
    template_name = 'apps/product-detail.html'
    context_object_name = 'product'


class LoginTemplateView(TemplateView):
    template_name = 'apps/auth/login.html'

    def post(self, request, *args, **kwargs):
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(request, email=email, password=password)
        if user:
            login(request, user)
            return redirect('product_list_page')

        return redirect('login_page')


class RegisterTemplateView(TemplateView):
    template_name = 'apps/auth/register.html'

    def post(self, request, *args, **kwargs):
        first_name = request.POST.get('first_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if User.objects.filter(email=email).exists() or password != confirm_password:
            print('XATOLIK')
            return redirect('register_page')
        User.objects.create_user(email=email, first_name=first_name, password=password)
        return redirect('login_page')


class ProfileTemplateView(LoginRequiredMixin, TemplateView):
    template_name = 'apps/auth/profile.html'
    login_url = reverse_lazy('login_page')


class CustomLogoutView(View):
    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect('product_list_page')
