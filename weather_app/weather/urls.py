from django.urls import path
from . import views  # Import the views module from the current app

urlpatterns = [
    path('', views.weather_view, name='weather_view'),  # Match the function name
]
