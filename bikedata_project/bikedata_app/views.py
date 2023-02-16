from django.shortcuts import render

from django.http import HttpResponse
# Create your views here.
import requests
from .models import BikeStation


def save_bike_data(request):
    url = 'http://api.citybik.es/v2/networks/bikesantiago'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        for station in data['network']['stations']:
            bike_station = BikeStation(name=station['name'], latitude=station['latitude'], longitude=station['longitude'], free_bikes=station['free_bikes'], empty_slots=station['empty_slots'])
            bike_station.save()
        return HttpResponse ('Datos de Bike Santiago almacenados exitosamente')
    else:
        return HttpResponse('Error al obtener los datos de Bike Santiago')

def bike_stations(request):
    bike_stations = BikeStation.objects.all()
    return render(request, 'bike_stations.html', {'bike_stations': bike_stations})