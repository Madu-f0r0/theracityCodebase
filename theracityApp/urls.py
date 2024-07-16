from django.urls import path
from . import views

urlpatterns = [
    path('theracity/', views.home_page, name='homepage'),
    path('theracity/about/', views.about_us, name='about_us'),
    path('theracity/user/location/', views.store_user_location, name='user_location'),
    path('theracity/user/pharmacies/', views.closest_pharmacies, name='closest_pharmacies'),
    path('theracity/search/medicine/suggest/<str:term>/', views.medicine_autosuggest, name='medicine_autosuggest'),
    path('theracity/search/medicine/<int:id>', views.pharmacies_with_medicine, name='pharmacies_with_medicine'),
    path('theracity/search/pharmacy/suggest/<str:term>/', views.pharmacies_autosuggest, name='pharmacies_autosuggest'),
    path('theracity/search/pharmacy/<int:id>', views.search_pharmacy, name='search_pharmacy'),
]
