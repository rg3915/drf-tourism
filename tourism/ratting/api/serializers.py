from rest_framework.serializers import ModelSerializer
from tourism.ratting.models import Ratting


class RattingSerializer(ModelSerializer):

    class Meta:
        model = Ratting
        fields = ('id', 'comment', 'user', 'note', 'created')
