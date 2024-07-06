from rest_framework import serializers, viewsets
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated

from gasolineria.api import SurtidorSimpleSerializer, BombaSimpleSerializer
from gasolineria.models import TipoCombustible, Surtidor, Bomba


class TipoCombustibleSerializer(serializers.ModelSerializer):
    surtidor = SurtidorSimpleSerializer(read_only=True)
    surtidor_id = serializers.PrimaryKeyRelatedField(
        queryset=Surtidor.objects.all(),
        source='surtidor',
        write_only=True)
    bomba = BombaSimpleSerializer(read_only=True)
    bomba_id = serializers.PrimaryKeyRelatedField(
        queryset=Bomba.objects.all(),
        source='bomba',
        write_only=True)

    class Meta:
        model = TipoCombustible
        fields = '__all__'


@permission_classes([IsAuthenticated])
class TipoCombustibleViewset(viewsets.ModelViewSet):
    serializer_class = TipoCombustibleSerializer
    queryset = TipoCombustible.objects.all()
