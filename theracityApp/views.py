from .models import Medicine, Pharmacy, Stock
from .forms import PharmacyRegistrationForm
from django.contrib.auth import login
from django.contrib.gis.geos import Point
from django.contrib.gis.db.models.functions import Distance
from django.contrib.sessions.models import Session
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST
import json


# Create your views here.
def home_page(request):
    """ Displays the homepage"""
    template = 'theracityApp/homepage.html'
    return render(request, template)


def about_us(request):
    """ Displays the about us page"""
    template = 'theracityApp/about.html'
    return render(request, template)


def register(request):
    if request.method == 'POST':
        form = PharmacyRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('homepage')
    else:
        form = PharmacyRegistrationForm()
    return render(request, 'theracityApp/register.html', {'form': form})


# Function to recieve user's coordinates
@require_POST
def store_user_location(request):
    try:
        request_data = json.loads(request.body.decode('utf-8'))
        longitude = request_data.get('longitude')
        latitude = request_data.get('latitude')

        # Store the coordinates in session variables
        request.session['user_longitude'] = longitude
        request.session['user_latitude'] = latitude

        return JsonResponse({'status': 'success', 'latitude': latitude, 'longitude': longitude})
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)


def closest_pharmacies(request):
    # Retrieve user's location from the session
    user_longitude = request.session.get('user_longitude')
    user_latitude = request.session.get('user_latitude')

    # Check if the user's location is available
    if user_latitude is None or user_longitude is None:
        return JsonResponse({'error': 'User location not available in session'}, status=400)

    # Create a Point object from the user's location
    user_location = Point(float(user_longitude), float(user_latitude), srid=4326)

    # Query db for five closest pharmacies
    closest_pharmacies = (
        Pharmacy.objects.annotate(
            distance=Distance('location', user_location)
        ).order_by('distance')[:5]
    )

    # Serialize the results if needed
    serialized_pharmacies = [{'name': pharmacy.name, 'distance': pharmacy.distance.m, 'id': pharmacy.id} for pharmacy in closest_pharmacies]

    # Return a JSON response containing the serialized data
    return JsonResponse({'closest_pharmacies': serialized_pharmacies})


def medicine_autosuggest(request, term):
    """Implements the medicine autosuggestion feature"""
    if not term:
        autosuggestions = []
    else:
        medicines = Medicine.objects.filter(medicine_name__icontains=term)
        autosuggestions = [{'medicine_name': medicine.medicine_name, 'medicine_id': medicine.id} for medicine in medicines]
    return JsonResponse({'autosuggestions': autosuggestions})


def pharmacies_with_medicine(request, id):
    """Returns the pharmacies closest to the user, stored the DB with the medicine in stock"""
    if not id:
        return JsonResponse({'error': 'Invalid medicine id'}, status=400)
    else:
        # Retrieve user's location from the session
        user_longitude = request.session.get('user_longitude')
        user_latitude = request.session.get('user_latitude')

        # Check if the user's location is available
        if user_latitude is None or user_longitude is None:
            return JsonResponse({'error': 'User location not available in the session'}, status=400)

        # Create a Point object from the user's location
        user_location = Point(float(user_longitude), float(user_latitude), srid=4326)

        # Query DB for medicine with specified id
        try:
            medicine = Medicine.objects.get(id=id)
        except Exception:
            return JsonResponse({'error': 'no medicine with this id in our database'}, status=404)

        #Query DB for 5 closest pharmacies with specified medicine
        pharmacies = Pharmacy.objects.filter(stock__medicine=medicine).annotate(
                distance=Distance('location', user_location)
            ).order_by('distance')[:5]

        # Serialize pharmacy and medicine details to return as response
        data = {
            'medicine': {
                'name': medicine.medicine_name,
                'manufacturer_name': medicine.manufacturer_name,
                'manufacturer_country': medicine.manufacturer_country,
            },
            'pharmacies': [
                {
                    'name': pharmacy.pharmacy_name,
                    'address': pharmacy.address,
                    'medicine_price': Stock.objects.filter(
                        pharmacy__id=pharmacy.id,
                        medicine_id=medicine.id).values_list('price', flat=True).first()
                } for pharmacy in pharmacies
            ]
        }

        return JsonResponse(data)


def pharmacies_autosuggest(request, term):
    """Implements the pharmacies autosuggestion feature"""
    if not term:
        autosuggestions = []
    else:
        pharmacies = Pharmacy.objects.filter(pharmacy_name__icontains=term)
        autosuggestions = [{'pharmacy_id': pharmacy.id, 'pharmacy_name': pharmacy.pharmacy_name, 'address': pharmacy.address} for pharmacy in pharmacies]
    return JsonResponse({'autosuggestions': autosuggestions})


def search_pharmacy(request, id):
    """Returns the details of the pharmacy with a specified id"""
    if not id:
        return JsonResponse({'error': 'Invalid medicine id'}, status=400)
    else:
        try:
            pharmacy = Pharmacy.objects.get(id=id)
        except Exception:
            return JsonResponse({'error': 'no pharmacy with this id in our database'}, status=404)

        context = {
            'name': pharmacy.pharmacy_name,
            'address': pharmacy.address,
            'lat': pharmacy.latitude,
            'lng': pharmacy.longitude,
        }

        template = 'theracityApp/pharmacy.html'
        return render(request, template, context)
