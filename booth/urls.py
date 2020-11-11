from . import views
from rest_framework.routers import DefaultRouter

booth_router = DefaultRouter()
booth_router.register(r'region', views.RegionViewSet)