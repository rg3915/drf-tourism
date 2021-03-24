from django.db import IntegrityError
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from tourism.core.models import TouristSpot

from .serializers import TouristSpotSerializer


def update_instance_from_dict(instance, attrs, save=False):
    for attr, val in attrs.items():
        setattr(instance, attr, val)
    if save:
        instance.save()
    return instance


class TouristSpotViewSet(ModelViewSet):
    """
    A simple ViewSet for viewing and editing accounts.
    """
    # queryset = TouristSpot.objects.all()
    serializer_class = TouristSpotSerializer

    # def get_queryset(self):
    #     # Return only approved TouristSpot.
    #     return TouristSpot.objects.filter(approved=True)

    def get_queryset(self):
        id = self.request.query_params.get('id', None)
        name = self.request.query_params.get('name', None)
        description = self.request.query_params.get('description', None)
        queryset = TouristSpot.objects.all()

        if id:
            queryset = queryset.filter(pk=id)

        if name:
            queryset = queryset.filter(name__icontains=name)

        if description:
            queryset = queryset.filter(description__icontains=description)

        return queryset

    # def list(self, request, *args, **kwargs):
    #     queryset = self.get_queryset()
    #     serializer = self.get_serializer(queryset, many=True)
    #     return Response(serializer.data)

    # def create(self, request, *args, **kwargs):
    #     try:
    #         return super().create(request, *args, **kwargs)
    #     except IntegrityError as e:
    #         return Response(
    #             data={
    #                 'error': 'Já existe, tente usar o método PUT',
    #                 'detail': f'{e}'
    #             },
    #             status=status.HTTP_500_INTERNAL_SERVER_ERROR
    #         )

    # def create(self, validated_data):
    #     ...

    def create(self, request, *args, **kwargs):
        return super(TouristSpotViewSet, self).create(request, *args, **kwargs)

    # def destroy(self, request, *args, **kwargs):
    #     instance = self.get_object()
    #     if not instance.can_delete():
    #         return Response(data={'detail': 'Cannot delete.'},
    #                         status=status.HTTP_403_FORBIDDEN)
    #     self.perform_destroy(instance)
    #     return Response(status=status.HTTP_204_NO_CONTENT)

    # def update(self, instance, validated_data):
    #     update_instance_from_dict(instance, validated_data)
    #     instance.save()
    #     return instance

    @action(methods=['get'], detail=True)
    def denounce(self, request, pk=None):
        return Response({'pk': pk})
