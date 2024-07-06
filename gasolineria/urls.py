from django.urls import path, include
from rest_framework import routers

from gasolineria.api import SurtidorViewset, BombaViewset, TipoCombustibleViewset

router = routers.DefaultRouter()

router.register(r'surtidor', SurtidorViewset)
router.register(r'bomba', BombaViewset)
router.register(r'tipocombustible', TipoCombustibleViewset)

urlpatterns = [
    path('', include(router.urls)),
]
