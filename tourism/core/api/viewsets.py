from django.db import IntegrityError
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import action
from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAuthenticated
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

    # permission_classes = (IsAuthenticated,)
    # DjangoModelPermissions
    # https://www.django-rest-framework.org/api-guide/permissions/#djangomodelpermissions
    # Você precisa dar as permissões para o usuário no painel de Admin.

    # authentication_classes = (TokenAuthentication,)

    filter_backends = (SearchFilter,)
    search_fields = ('name', 'description', 'address__address', 'address__city')
    # O lookup_field default é o id. E o novo lookup_field deve ser unique=True.
    # lookup_field = 'nome'

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

    @action(methods=['post'], detail=True)
    def associated_attractions(self, request, pk):
        attractions = request.data['ids']
        tourist_spot = TouristSpot.objects.get(pk=pk)
        tourist_spot.attractions.set(attractions)
        tourist_spot.save()
        serializer = self.get_serializer(tourist_spot)
        return Response(serializer.data)
