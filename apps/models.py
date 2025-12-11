from django.contrib.auth.models import AbstractUser
from django.db.models import Model, CharField, IntegerField, ImageField, ForeignKey, CASCADE, SlugField, \
    PositiveIntegerField, DateTimeField, FloatField, ManyToManyField, EmailField
from django.utils.text import slugify
from django.utils.timezone import now
from django_ckeditor_5.fields import CKEditor5Field
from django_jsonform.models.fields import JSONField

from apps.managers import CustomUserManager


class Category(Model):
    name = CharField(max_length=255)

    def __str__(self):
        return f"{self.id} - {self.name}"


class Tag(Model):
    name = CharField(max_length=255)
    slug = SlugField(max_length=255, editable=False, unique=True)

    def save(self, *, force_insert=False, force_update=False, using=None, update_fields=None):
        self.slug = slugify(self.name)
        super().save(force_insert=force_insert, force_update=force_update, using=using, update_fields=update_fields)

    def __str__(self):
        return self.name


class ProductImage(Model):
    product = ForeignKey('apps.Product', CASCADE, related_name='images')
    image = ImageField(upload_to='products/%Y/%m/%d')


class Product(Model):
    ITEMS_SCHEMA = {
        "type": "array",
        "items": {
            "type": "object",
            "keys": {
                "key": {"type": "string"},
                "value": {"type": "string"}
            }
        }
    }
    name = CharField(max_length=255)
    slug = SlugField(max_length=255, editable=False, unique=True)
    shipping_cost = IntegerField()
    price = FloatField()
    discount_percentage = IntegerField()

    quantity = PositiveIntegerField()
    tags = ManyToManyField('apps.Tag', related_name='products', blank=True)
    category = ForeignKey('apps.Category', CASCADE, related_name='products')
    like_count = PositiveIntegerField(default=0)
    specifications = JSONField(schema=ITEMS_SCHEMA, blank=True)
    short_description = CKEditor5Field()
    description = CKEditor5Field()
    updated_at = DateTimeField(auto_now_add=True)
    created_at = DateTimeField(auto_now=True)

    def save(self, *, force_insert=False, force_update=False, using=None, update_fields=None):
        self.slug = slugify(self.name)
        super().save(force_insert=force_insert, force_update=force_update, using=using, update_fields=update_fields)

    @property
    def discount_price(self):
        return self.price - self.price * self.discount_percentage / 100

    @property
    def available_quantity(self):
        return self.quantity > 0

    @property
    def is_new(self):
        return self.created_at > now().replace(hour=0, minute=0, second=0)


class User(AbstractUser):
    email = EmailField("email address", unique=True)
    username = None

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
