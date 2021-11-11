from rest_framework import serializers

from .models import Player, Season

class SeasonSeralizer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Season
        fields = ('player', 'year', 'ppg', 'rpg','apg','spg')

class PlayerSerializer(serializers.HyperlinkedModelSerializer):
    seasons = SeasonSeralizer(many=True, read_only=True)      
    class Meta:
        model = Player
        fields = ('first_name', 'last_name', 'jersey_number','seasons')
