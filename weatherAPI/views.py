
# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
import requests

def index(request):
    api_key = '3C8TRCWYPKSPU83H6U8CJ5CUR'
    location  = request.GET.get('location')
    print(location)
    url = f'https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{location}?unitGroup=us&key={api_key}&contentType=json'

    response = requests.get(url)
    weather_data = response.json()

    return render(request, 'main.html', {'weatherData': weather_data})