"""bikedata_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from bikedata_app.views import save_bike_data
from bikedata_app.views import bike_stations

urlpatterns = [
    path('admin/', admin.site.urls),
    path('save_bike_data/', save_bike_data, name='save_bike_data'),
    path('bike-stations/', bike_stations, name='bike_stations'),
]
