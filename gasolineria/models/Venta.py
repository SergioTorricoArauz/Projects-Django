from django.db import models

from gasolineria.models import TipoCombustible, Bomba


class Venta(models.Model):
    nombre_factura = models.CharField(max_length=100)
    nit_factura = models.CharField(max_length=50)
    cliente = models.CharField(max_length=100)
    correo = models.EmailField()
    monto = models.FloatField()
    precio_actual_producto = models.FloatField()
    cantidad_producto_litros = models.FloatField()
    tipo_producto = models.ForeignKey(TipoCombustible, on_delete=models.CASCADE)
    bomba = models.ForeignKey(Bomba, on_delete=models.CASCADE)
    fecha_hora = models.DateTimeField(auto_now_add=True, blank=True)
