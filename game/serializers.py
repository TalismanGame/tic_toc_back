from importlib.metadata import requires
from rest_framework import serializers

from tic_toc_back.settings import REQUIRED_ERROR_KEY
from .models import Player, Game


class CreateGameSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Game
        fields = '__all__'

class JoinGameSerializer(serializers.Serializer):
    # use model serializers to find object and pass instance to view and change it
    inviteCode = serializers.CharField(min_length=9, required=True)

    # class Meta:
    #     model = Game
    #     fields = ['inviteCode']
        
    #     # ******** 
    #     # this is a good way of handing errors and validate data in 
    #     # serializer than setup custom error response. 
    #     # so use this and make sure you config all in settings as well 
    #     # ********
    #     extra_kwargs = {
    #         'inviteCode': {
    #             'required': True,
    #             "min_length": 9,
    #         }
    #     }

# class UpdateGameDataSerializer(serializers.Serializer):
#     inviteCode = serializers.CharField(min_length=9, required=True)
    # this is wrong


class GetGameDataSerializer(serializers.ModelSerializer):
    playerX = serializers.StringRelatedField()
    playerO = serializers.StringRelatedField()

    class Meta:
        model = Game
        fields = '__all__'