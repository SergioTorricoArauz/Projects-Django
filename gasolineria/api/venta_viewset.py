from rest_framework import serializers, viewsets
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated

from gasolineria.models import Venta


class VentaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Venta
        fields = '__all__'


@permission_classes([IsAuthenticated])
class VentaViewset(viewsets.ModelViewSet):
    serializer_class = VentaSerializer
    queryset = Venta.objects.all()
