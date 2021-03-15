from rest_framework.serializers import ModelSerializer
from tourism.core.models import Attraction


class AttractionSerializer(ModelSerializer):

    class Meta:
        model = Attraction
        fields = ('id', 'name', 'description', 'opening_hours', 'min_age')
