from django.db.models import Model, CharField, IntegerField, ImageField, ForeignKey, CASCADE, SlugField, \
    PositiveIntegerField, DateTimeField, FloatField, TextField, ManyToManyField, JSONField
from django_ckeditor_5.fields import CKEditor5Field


class Category(Model):
    name = CharField(max_length=255)

    def __str__(self):
        return f"{self.id} - {self.name}"


class Tag(Model):
    name = CharField(max_length=255)
    slug = SlugField(max_length=255, null=True, unique=True)


class Product(Model):
    name = CharField(max_length=255)
    slug = SlugField(max_length=255, null=True, unique=True)
    shipping_cost = IntegerField()
    price = FloatField()
    discount_percentage = IntegerField()

    quantity = PositiveIntegerField()
    tags = ManyToManyField('apps.Tag', related_name='products', blank=True)
    category = ForeignKey('apps.Category', CASCADE, related_name='products')
    like_count = PositiveIntegerField(default=0)
    specifications = JSONField(default=dict, blank=True)
    short_description = CKEditor5Field()
    description = CKEditor5Field()
    updated_at = DateTimeField(auto_now_add=True)
    created_at = DateTimeField(auto_now=True)


class ProductImage(Model):
    product = ForeignKey('apps.Product', CASCADE, related_name='images')
    image = ImageField(upload_to='products/%Y/%m/%d')
