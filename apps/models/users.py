from django.contrib.auth.models import AbstractUser
from django.db.models import EmailField, ImageField
from django.db.models.fields import BooleanField

from apps.managers import CustomUserManager


class User(AbstractUser):
    email = EmailField("email address", unique=True)
    image = ImageField(upload_to='users/images/%Y/%m/%d', blank=True, null=True)
    banner = ImageField(upload_to='users/banners/%Y/%m/%d', blank=True, null=True)
    is_active = BooleanField(default=False)
    username = None

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    @property
    def is_valid_password(self):
        return self.has_usable_password()
