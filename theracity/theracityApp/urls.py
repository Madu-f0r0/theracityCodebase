from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page),
    path('user_location/', views.store_user_location),
    path('hello/', views.say_hello),
]