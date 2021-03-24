from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer

from tourism.address.api.serializers import AddressSerializer
from tourism.attraction.api.serializers import AttractionSerializer
from tourism.core.models import TouristSpot


class TouristSpotSerializer(ModelSerializer):
    attractions = AttractionSerializer(many=True)
    address = AddressSerializer()
    full_description = SerializerMethodField()

    class Meta:
        model = TouristSpot
        fields = (
            'id',
            'name',
            'description',
            'full_description',
            'complete_description',
            'approved',
            'photo',
            'attractions',
            'comments',
            'rattings',
            'address',
        )

    def get_full_description(self, obj):
        return f'{obj.name} - {obj.description}'
