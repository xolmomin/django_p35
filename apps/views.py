from django.views.generic import ListView, DetailView

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
