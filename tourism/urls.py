from django.urls import include, path
from django.contrib import admin
from rest_framework import routers
from tourism.core.api.viewsets import TouristSpotViewSet


router = routers.DefaultRouter()
router.register(r'ponto-turistico', TouristSpotViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
]
