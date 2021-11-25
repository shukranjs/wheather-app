from django.shortcuts import render
import requests

def wheather(request):
    city = request.GET.get('city')
    # api.openweathermap.org/data/2.5/weather?q={city name}&appid={API key}
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid=edbb07470ba0020620021938bf832958'
    city_weather = requests.get(url.format(city)).json()
    print(city_weather)
    return render(request, 'wheather.html', {'city_weather': city_weather['weather'][0]['description'], 'city': city})



