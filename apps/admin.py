from django.contrib import admin

from apps.models import Category, Product, Testing


@admin.register(Testing)
class TestingModelAdmin(admin.ModelAdmin):
    pass


@admin.register(Category)
class CategoryModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'product_count']
    search_fields = ['name']
    list_per_page = 5
    ordering = ['id']

    @admin.display(description='Product count')
    def product_count(self, obj: Category):
        return obj.products.count()


@admin.register(Product)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'category__name']
