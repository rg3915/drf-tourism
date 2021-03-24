from rest_framework.serializers import ModelSerializer

from tourism.address.api.serializers import AddressSerializer
from tourism.attraction.api.serializers import AttractionSerializer
from tourism.core.models import TouristSpot


class TouristSpotSerializer(ModelSerializer):
    attractions = AttractionSerializer(many=True)
    address = AddressSerializer()

    class Meta:
        model = TouristSpot
        fields = (
            'id',
            'name',
            'description',
            'approved',
            'photo',
            'attractions',
            'comments',
            'rattings',
            'address',
        )
