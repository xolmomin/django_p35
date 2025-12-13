from django.urls import path

from apps.views import ProductListView, ProductDetailView, RegisterCreateView, CustomLoginView, ProfileTemplateView, \
    CustomLogoutView, GoogleLoginView, GoogleCallbackView

urlpatterns = [
    path('', ProductListView.as_view(), name='product_list_page'),
    path('products/<slug:slug>', ProductDetailView.as_view(), name='product_detail_page'),

    path('auth/profile', ProfileTemplateView.as_view(), name='profile_page'),
    path('auth/register', RegisterCreateView.as_view(), name='register_page'),
    path('auth/login', CustomLoginView.as_view(), name='login_page'),
    path('auth/logout', CustomLogoutView.as_view(), name='logout_page'),

    path("auth/google-login", GoogleLoginView.as_view(), name='google_login_page'),
    path("auth/oauth2/callback", GoogleCallbackView.as_view(), name='google_callback_page'),
]
