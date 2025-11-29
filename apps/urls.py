from django.urls import path

from apps.views import index_page

urlpatterns = [
    path('', index_page)
]
