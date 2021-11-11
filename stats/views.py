
from rest_framework import viewsets

from .serializers import PlayerSerializer, SeasonSeralizer
from .models import Player, Season


class PlayerViewSet(viewsets.ModelViewSet):
    queryset = Player.objects.all().order_by('last_name')
    serializer_class = PlayerSerializer



class SeasonViewSet(viewsets.ModelViewSet):
    queryset = Season.objects.all().order_by('player')
    serializer_class = SeasonSeralizer

