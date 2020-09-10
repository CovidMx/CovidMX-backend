from django.urls import path
from . import views

urlpatterns = [
    path('api/EstadisticasPorEdad/',views.ListEstadisticasPorEdad.as_view(),),
    path('api/Entidades/',views.ListEntidades.as_view(),),
    path('api/CasosPorEstado/',views.ListCasosPorEstado.as_view()),
    path('api/Municipios/',views.ListMunicipios.as_view()),
    path('api/CasosPorMunicipio/',views.ListCasosPorMunicipio.as_view())
]
