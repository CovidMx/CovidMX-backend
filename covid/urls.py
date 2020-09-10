from django.urls import path
from . import views

urlpatterns = [
    path('api/',views.covidListApiView.as_view())    
]
