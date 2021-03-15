from rest_framework.serializers import ModelSerializer
from tourism.address.models import Address


class AddressSerializer(ModelSerializer):

    class Meta:
        model = Address
        fields = (
            'id',
            'address',
            'address_number',
            'complement',
            'district',
            'city',
            'uf',
            'cep',
            'country',
            'latitude',
            'longitude',
        )
