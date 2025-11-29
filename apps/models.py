from django.db import models
from django.db.models import DateTimeField


class Student(models.Model):
    first_name = models.CharField(max_length=100)  # varchar(100)
    last_name = models.CharField(max_length=100)  # varchar(100)
    phone = models.CharField(max_length=100)  # varchar(100)
    address = models.CharField(max_length=100)  # varchar(100)
    birth_date = models.DateField()
    registered_at = models.DateTimeField()

    def __str__(self):
        return self.first_name + " " + self.last_name


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100)
    short_description = models.CharField(max_length=255, blank=True)
    price = models.IntegerField()
    category = models.ForeignKey('apps.Category', models.CASCADE)
    image = models.ImageField(upload_to='products/%Y/%m/%d')
    created_at = DateTimeField(auto_now_add=True)
