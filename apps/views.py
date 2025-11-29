from django.shortcuts import render

from apps.models import Product


# function based, class based

def index_page(request):
    products = Product.objects.all()

    context = {
        'products': products
    }
    return render(request, 'apps/product-list.html', context)
