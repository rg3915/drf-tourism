from rest_framework.viewsets import ModelViewSet
from tourism.ratting.models import Ratting
from .serializers import RattingSerializer


class RattingViewSet(ModelViewSet):
    queryset = Ratting.objects.all()
    serializer_class = RattingSerializer
