from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import views as auth_views
from .views import product_create_view, product_detail_view, index_view, register_view, home_view, ProductUpdateView, ProductDeleteView

urlpatterns = [
    path('', index_view, name='index'),
    path('login/', auth_views.LoginView.as_view(template_name='products_listing/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('create/', product_create_view, name='product_create'),
    path('product/<int:pk>/', product_detail_view, name='product_detail'),
    path('register/', register_view, name='register'),
    path('password-reset/', auth_views.PasswordResetView.as_view(template_name='products_listing/password_reset_form.html'), name='password_reset'),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='products_listing/password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='products_listing/password_reset_confirm.html'), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='products_listing/password_reset_complete.html'), name='password_reset_complete'),
    path('edit/<int:pk>/', ProductUpdateView.as_view(), name='edit_product'),
    path('delete/<int:pk>/', ProductDeleteView.as_view(), name='delete_product'),
    path('', home_view, name='product_list'),
]