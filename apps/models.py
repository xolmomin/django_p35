from django.db import models
from django.db.models import DateTimeField


class Testing(models.Model):
    class Valijon(models.TextChoices):
        FRESHMAN = "FR", "Freshman"
        SOPHOMORE = "SO", "Sophomore"
        JUNIOR = "JR", "Junior"
        SENIOR = "SR", "Senior"
        GRADUATE = "GR", "Graduate"

    is_active = models.BooleanField(default=False, db_default=False, db_index=True)
    year_in_school = models.CharField(
        max_length=2,
        choices=Valijon.choices,
        default=Valijon.FRESHMAN, help_text="1tasini tanlash kerak",
        verbose_name="Maktab"
    )

    # name = models.CharField(max_length=120, editable=False)
    class Meta:
        verbose_name = "Vali table"
        verbose_name_plural = "Vali tables"
        db_table = 'valijon_table'
        unique_together = ('is_active', 'year_in_school')


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

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return f"{self.id} - {self.name}"


class Product(models.Model):
    name = models.CharField(max_length=100)
    short_description = models.CharField(max_length=255, blank=True)
    price = models.IntegerField()
    category = models.ForeignKey('apps.Category', models.CASCADE, related_name='products')
    image = models.ImageField(upload_to='products/%Y/%m/%d')
    created_at = DateTimeField(auto_now_add=True)
