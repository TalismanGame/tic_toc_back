from importlib.metadata import requires
from rest_framework import serializers

from tic_toc_back.settings import REQUIRED_ERROR_KEY
from .models import Player, Game


class CreateGameSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Game
        fields = '__all__'


class JoinGameSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Game
        fields = '__all__'
        extra_kwargs = {
            'inviteCode': {
                'required': True,
                "min_length": 3,
            }
        }