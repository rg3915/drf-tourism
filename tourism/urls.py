from django.urls import include, path
from django.contrib import admin
from rest_framework import routers
from tourism.core.api.viewsets import TouristSpotViewSet
from tourism.attraction.api.viewsets import AttractionViewSet


router = routers.DefaultRouter()
router.register(r'tourists-spots', TouristSpotViewSet)
router.register(r'attractions', AttractionViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
]
