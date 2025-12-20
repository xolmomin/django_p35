from time import sleep

from celery import shared_task
from django.core.mail import send_mail

from root.settings import EMAIL_HOST_USER


@shared_task
def add(x, y):
    return x + y


@shared_task
def mul(x, y):
    return x * y


@shared_task
def _send_to_email(subject: str, msg: str, email: str | list):
    if isinstance(email, str):
        email = [email]
    sleep(3)

    return {"message": msg, "email": email}
    # send_mail(subject, msg, EMAIL_HOST_USER, email)


@shared_task
def send_registration_email(email):
    subject = 'Registration email'
    message = 'siz royhat otdiz!'

    return _send_to_email(subject, message, email)
