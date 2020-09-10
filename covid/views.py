from django.shortcuts import render

from rest_framework.generics import ListAPIView

from .models import (    
    EstadisticasPorEdadModel,
    CasosPorEstadoModel,
    CasosPorMunicipioModel,
    EntidadesModel,
    MunicipiosModel
)


from .serializers import (
    EstadisticasPorEdadSerializer,
    CasosPorEstadoSerializer,
    CasosPorMunicipioSerializer,
    EntidadesSerializer,
    MunicipiosSerializer
)

# Create your views here.


class ListEstadisticasPorEdad(ListAPIView):
    serializer_class = EstadisticasPorEdadSerializer

    def get_queryset(self):
        return EstadisticasPorEdadModel.objects.all()

class ListCasosPorEstado(ListAPIView):
    serializer_class = CasosPorEstadoSerializer

    def get_queryset(self):
        return CasosPorEstadoModel.objects.all()

class ListCasosPorMunicipio(ListAPIView):
    serializer_class = CasosPorMunicipioSerializer

    def get_queryset(self):
        return CasosPorMunicipioModel.objects.all()

class ListEntidades(ListAPIView):
    serializer_class = EntidadesSerializer

    def get_queryset(self):
        return EntidadesModel.objects.all()

class ListMunicipios(ListAPIView):
    serializer_class = MunicipiosSerializer

    def get_queryset(self):
        return MunicipiosModel.objects.all()  
    
    
    
    
    