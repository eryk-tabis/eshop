from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .forms import PasswordChangeForm
urlpatterns = [
    path('login/', views.login_page, name='login_view'),
    path('register/', views.register_page, name='register_view'),
    path('logout/', views.logout_user, name='logout'),
    path('password-reset/', views.password_reset, name='password_reset'),
    path('password-reset/done/', views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', views.PasswordResetConfirmView.as_view(),  name='password_reset_confirm'),
    path('reset/done/', views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]