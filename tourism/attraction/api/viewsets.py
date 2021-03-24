from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.viewsets import ModelViewSet

from tourism.attraction.models import Attraction

from .serializers import AttractionSerializer


class AttractionViewSet(ModelViewSet):
    # https://www.django-rest-framework.org/api-guide/filtering/#generic-filtering
    queryset = Attraction.objects.all()
    serializer_class = AttractionSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('name', 'description')
