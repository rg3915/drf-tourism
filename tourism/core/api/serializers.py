from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer

from tourism.address.api.serializers import AddressSerializer
from tourism.address.models import Address
from tourism.attraction.api.serializers import AttractionSerializer
from tourism.attraction.models import Attraction
from tourism.core.models import TouristSpot


class TouristSpotSerializer(ModelSerializer):
    # attractions = AttractionSerializer(many=True, read_only=True)
    attractions = AttractionSerializer(many=True)
    # address = AddressSerializer(read_only=True)
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
        read_only_fields = ('comments', 'rattings')

    def create_attractions(self, attractions, tourist_spot):
        for attraction in attractions:
            obj = Attraction.objects.create(**attraction)
            tourist_spot.attractions.add(obj)

    def create(self, validated_data):
        attractions = validated_data.pop('attractions')
        address = validated_data.pop('address')

        tourist_spot = TouristSpot.objects.create(**validated_data)
        self.create_attractions(attractions, tourist_spot)

        address_obj = Address.objects.create(**address)
        tourist_spot.address = address_obj
        tourist_spot.save()

        return tourist_spot

    def get_full_description(self, obj):
        return f'{obj.name} - {obj.description}'
