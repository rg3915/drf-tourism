from django.urls import include, path
from django.contrib import admin
from rest_framework import routers
from tourism.core.api.viewsets import TouristSpotViewSet
from tourism.attraction.api.viewsets import AttractionViewSet
from tourism.address.api.viewsets import AddressViewSet
from tourism.comment.api.viewsets import CommentViewSet
from tourism.ratting.api.viewsets import RattingViewSet


router = routers.DefaultRouter()
router.register(r'tourists-spots', TouristSpotViewSet)
router.register(r'attractions', AttractionViewSet)
router.register(r'adresses', AddressViewSet)
router.register(r'comments', CommentViewSet)
router.register(r'rattings', RattingViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
]