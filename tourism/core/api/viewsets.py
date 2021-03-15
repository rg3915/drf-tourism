from rest_framework.viewsets import ModelViewSet
from tourism.core.models import TouristSpot
from .serializers import TouristSpotSerializer


class TouristSpotViewSet(ModelViewSet):
    """
    A simple ViewSet for viewing and editing accounts.
    """
    queryset = TouristSpot.objects.all()
    serializer_class = TouristSpotSerializer
