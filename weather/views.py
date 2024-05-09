# weather/views.py

from django.shortcuts import render
import requests

def home(request):
    if request.method == 'POST':
        city = request.POST['city']
        api_key = '0b8329743de4d332bd34b26c31596667'
        url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid=0b8329743de4d332bd34b26c31596667&units=metric'
        response = requests.get(url)
        data = response.json()

        context = {
            'city': city,
            'temperature': data['main']['temp'],
            'description': data['weather'][0]['description'],
            'humidity': data['main']['humidity'],
            'wind_speed': data['wind']['speed']
        }
        return render(request, 'weather1/home.html', context)
    else:
        return render(request, 'weather1/home.html')


# Create your views here.
