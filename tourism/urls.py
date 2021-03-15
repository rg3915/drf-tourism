from django.urls import include, path
from django.contrib import admin
from rest_framework import routers
from django.conf import settings
from django.conf.urls.static import static

from tourism.core.api.viewsets import TouristSpotViewSet
from tourism.attraction.api.viewsets import AttractionViewSet
from tourism.address.api.viewsets import AddressViewSet
from tourism.comment.api.viewsets import CommentViewSet
from tourism.ratting.api.viewsets import RattingViewSet


router = routers.DefaultRouter()
router.register(r'tourists-spots', TouristSpotViewSet, basename='tourist_spot')
router.register(r'attractions', AttractionViewSet)
router.register(r'adresses', AddressViewSet)
router.register(r'comments', CommentViewSet)
router.register(r'rattings', RattingViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# https://docs.djangoproject.com/en/3.1/howto/static-files/#serving-static-files-during-development
