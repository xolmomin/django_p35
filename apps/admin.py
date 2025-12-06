from django.contrib import admin

from apps.models import Product, Category, ProductImage


@admin.register(Category)
class CategoryModelAdmin(admin.ModelAdmin):
    pass


class ProductImageStackedInline(admin.StackedInline):
    model = ProductImage
    min_num = 1
    extra = 0


@admin.register(Product)
class ProductModelAdmin(admin.ModelAdmin):
    readonly_fields = ['slug', 'like_count']
    inlines = [ProductImageStackedInline]
    list_display = ['id', 'name', 'price', 'discount_percentage', 'created_at']
