from django.urls import path, include

from rest_framework import routers
from . import views

router=routers.DefaultRouter()
router.register(r'players',views.PlayerViewSet)
router.register(r'seasons',views.SeasonViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]


