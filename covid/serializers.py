from rest_framework import serializers

from .models import (
    EstadisticasPorEdadModel, 
    CasosPorEstadoModel, 
    CasosPorMunicipioModel,
    EntidadesModel,
    MunicipiosModel
)

class EstadisticasPorEdadSerializer(serializers.ModelSerializer):
    class Meta:
        model = EstadisticasPorEdadModel
        fields = ('__all__')

class CasosPorEstadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CasosPorEstadoModel
        fields = ('__all__')

class CasosPorMunicipioSerializer(serializers.ModelSerializer):
    class Meta:
        model = CasosPorMunicipioModel
        fields = ('__all__')

class EntidadesSerializer(serializers.ModelSerializer):
    class Meta:
        model = EntidadesModel
        fields = ('__all__')

class MunicipiosSerializer(serializers.ModelSerializer):
    class Meta:
        model = MunicipiosModel
        fields = ('__all__')

