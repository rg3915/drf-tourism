from rest_framework.viewsets import ModelViewSet

from tourism.comment.models import Comment

from .serializers import CommentSerializer


class CommentViewSet(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
