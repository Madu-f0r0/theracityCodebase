from .models import Medicine, Pharmacy, Stock
from django.contrib.gis.geos import Point
from django.contrib.gis.db.models.functions import Distance
from django.contrib.sessions.models import Session
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.decorators.http import require_POST
import json


# Create your views here.
def say_hello(request):
    template = 'theracityApp/hello.html'
    context = {
        'name': 'Danny',
    }
    return render(request, template, context)
    # return HttpResponse('Hello world')

def home_page(request):
    """ Displays the homepage"""
    template = 'theracityApp/homepage.html'
    return render(request, template)

# Functiion to recieve user's coordinates
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
    serialized_pharmacies = [{'name': pharmacy.name, 'distance': pharmacy.distance.m} for pharmacy in closest_pharmacies]

    # Return a JSON response containing the serialized data
    return JsonResponse({'closest_pharmacies': serialized_pharmacies})
