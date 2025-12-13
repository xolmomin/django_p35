from django.contrib.auth.hashers import make_password
from django.core.exceptions import ValidationError
from django.forms import ModelForm
from django.forms.fields import EmailField, CharField
from django.forms.widgets import TextInput, PasswordInput

from apps.models import User


class RegisterModelForm(ModelForm):
    first_name = CharField(max_length=255)
    email = EmailField()
    password = CharField(max_length=128)
    confirm_password = CharField(max_length=128)

    class Meta:
        model = User
        fields = ['first_name', 'email', 'password']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise ValidationError("Bunaqa pochta ro'yhatdan o'tgan")
        return email

    def clean(self):
        password = self.cleaned_data.get("password")
        confirm_password = self.cleaned_data.get("confirm_password")
        if password != confirm_password:
            raise ValidationError("Parollar mos kelmadi!")
        self.cleaned_data["password"] = make_password(password)
        return self.cleaned_data
