from django.db import models

from gasolineria.models import Surtidor, Bomba


class TipoCombustible(models.Model):
    nombre = models.CharField(max_length=50)
    surtidor = models.ForeignKey(Surtidor, on_delete=models.CASCADE)
    bomba = models.ForeignKey(Bomba, on_delete=models.CASCADE)
    precio = models.FloatField()
    stock = models.FloatField()

    def reducir_stock(self, cantidad):
        if self.stock >= cantidad:
            self.stock -= cantidad
            self.save()
        else:
            raise ValueError("La cantidad a reducir es mayor que el stock disponible.")


def __str__(self):
    return self.nombre
