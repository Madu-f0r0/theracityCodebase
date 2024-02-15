from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name='homepage'),
    path('about/', views.about_us, name='about_us'),
    path('pharmacy/', views.pharmacy, name='pharmacy'),
    path('user/location/', views.store_user_location, name='user_location'),
    path('user/pharmacies/', views.closest_pharmacies, name='closest_pharmacies'),
    path('search/medicine/suggest/<str:term>/', views.medicine_autosuggest, name='medicine_autosuggest'),
    path('search/medicine/<int:id>', views.pharmacies_with_medicine, name='pharmacies_with_medicine'),
    path('search/pharmacy/suggest/<str:term>/', views.pharmacies_autosuggest, name='pharmacies_autosuggest'),
    path('search/pharmacy/<int:id>', views.search_pharmacy, name='search_pharmacy'),
    path('pharmacy-details/<int:id>', views.pharmacy_details, name='pharmacy-details'),
    path('hello/', views.say_hello, name='hello'),
]