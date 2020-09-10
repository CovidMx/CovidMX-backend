from django.shortcuts import render

from rest_framework.generics import ListAPIView

from .models import covidModel
from .serializers import CovidSerializer

# Create your views here.


class covidListApiView(ListAPIView):

    
    serializer_class = CovidSerializer

    def get_queryset(self):
        return covidModel.objects.all()
    