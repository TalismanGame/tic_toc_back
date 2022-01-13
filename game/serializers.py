from rest_framework import serializers
from .models import Player, Game


class CreateGameSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Game
        fields = '__all__'