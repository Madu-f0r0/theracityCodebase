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

# Functiion to recieve user's coordinates
""" @require_POST
def store_user_location(request):
    try:
        request_data = json.loads(request.body.decode('utf-8'))
        longitude = request_data.get('longitude')
        latitude = request_data.get('latitude')

        # Store the coordinates in session variables
        request.session['user_longitude'] = longitude
        request.session['user_latitude'] = latitude

        return JsonResponse({'status': 'success'})
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500) """