from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page),
    path('user/location/', views.store_user_location),
    path('user/pharmacies/', views.closest_pharmacies),
    path('search/medicine/suggest/<str:term>/', views.medicine_autosuggest),
    path('search/medicine/<int:id>', views.pharmacies_with_medicine),
    path('search/pharmacy/suggest/<str:term>/', views.pharmacies_autosuggest),
    path('search/pharmacy/', views.search_pharmacy),
    path('hello/', views.say_hello),
]