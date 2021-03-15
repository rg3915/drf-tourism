from rest_framework.serializers import ModelSerializer
from tourism.comment.models import Comment


class CommentSerializer(ModelSerializer):

    class Meta:
        model = Comment
        fields = ('id', 'comment', 'approved', 'created')
