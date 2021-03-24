from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer

from tourism.address.api.serializers import AddressSerializer
from tourism.attraction.api.serializers import AttractionSerializer
from tourism.core.models import TouristSpot
from tourism.attraction.models import Attraction


class TouristSpotSerializer(ModelSerializer):
    # attractions = AttractionSerializer(many=True, read_only=True)
    attractions = AttractionSerializer(many=True)
    address = AddressSerializer(read_only=True)
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
        read_only_fields = ('comments', 'rattings')

    def create_attractions(self, attractions, tourist_spot):
        for attraction in attractions:
            obj = Attraction.objects.create(**attraction)
            tourist_spot.attractions.add(obj)

    def create(self, validated_data):
        attractions = validated_data['attractions']
        del validated_data['attractions']
        tourist_spot = TouristSpot.objects.create(**validated_data)
        self.create_attractions(attractions, tourist_spot)
        return tourist_spot

    def get_full_description(self, obj):
        return f'{obj.name} - {obj.description}'
