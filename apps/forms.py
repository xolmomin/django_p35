from apps.models import User
from django.contrib.auth.hashers import make_password
from django.core.exceptions import ValidationError
from django.forms import ModelForm
from django.forms.fields import CharField, EmailField


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

# class CustomPasswordChangeForm(PasswordChangeForm):
#     @sensitive_variables("old_password")
#     def clean_old_password(self):
#         """
#         Validate that the old_password field is correct.
#         """
#         old_password = self.cleaned_data["old_password"]
#         if not self.user.check_password(old_password):
#             raise ValidationError(
#                 self.error_messages["password_incorrect"],
#                 code="password_incorrect",
#             )
#         return old_password
