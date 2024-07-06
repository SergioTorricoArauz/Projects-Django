from rest_framework import serializers, viewsets
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated

from gasolineria.api import SurtidorSimpleSerializer
from gasolineria.models import Bomba, Surtidor


class BombaSerializer(serializers.ModelSerializer):
    surtidor = SurtidorSimpleSerializer(read_only=True)
    surtidor_id = serializers.PrimaryKeyRelatedField(
        queryset=Surtidor.objects.all(),
        source='surtidor',
        write_only=True)

    class Meta:
        model = Bomba
        fields = ['id', 'surtidor', 'surtidor_id', 'codigo']


@permission_classes([IsAuthenticated])
class BombaViewset(viewsets.ModelViewSet):
    serializer_class = BombaSerializer
    queryset = Bomba.objects.all()
