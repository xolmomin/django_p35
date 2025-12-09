from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, TemplateView

from apps.models import Product


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


class RegisterTemplateView(TemplateView):
    template_name = 'apps/auth/register.html'


class ProfileTemplateView(LoginRequiredMixin, TemplateView):
    template_name = 'apps/auth/profile.html'
    login_url = reverse_lazy('login_page')
