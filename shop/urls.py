from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main_view'),
    path('training-programs/', views.training_programs, name='training_programs_view'),
    path('training-programs/<slug:slug>', views.training_programs_item, name='training_programs_item_view'),
    path('about-me/', views.about_me, name='about_me_view'),
    path('profile/', views.profile, name='profile_view'),
]
