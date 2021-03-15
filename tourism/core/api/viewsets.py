from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from tourism.core.models import TouristSpot
from .serializers import TouristSpotSerializer


class TouristSpotViewSet(ModelViewSet):
    """
    A simple ViewSet for viewing and editing accounts.
    """
    # queryset = TouristSpot.objects.all()
    serializer_class = TouristSpotSerializer

    def get_queryset(self):
        # Return only approved TouristSpot.
        return TouristSpot.objects.filter(approved=True)

    def list(self, request, *args, **kwargs):
        # Você pode sobrescrever o método list.
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
