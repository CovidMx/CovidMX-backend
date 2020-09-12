from django.contrib import admin
from .models import (
    EstadisticasPorEdadModel, 
    CasosPorEstadoModel,
    EntidadesModel,
    MunicipiosModel,
    CasosPorMunicipioModel
)

# Register your models here.

admin.site.register(EstadisticasPorEdadModel)
admin.site.register(CasosPorEstadoModel)
admin.site.register(CasosPorMunicipioModel)
admin.site.register(EntidadesModel)
admin.site.register(MunicipiosModel)