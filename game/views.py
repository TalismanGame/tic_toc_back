from ast import alias
from rest_framework import viewsets, permissions, status
from .models import Player, Game
from .serializers import CreateGameSerializer, JoinGameSerializer
from rest_framework.response import Response
from .utils import GenerateInviteCode

# Create your views here.

class CreateGameView(viewsets.ModelViewSet):
    serializer_class = CreateGameSerializer
    permission_classes = [permissions.IsAuthenticated]

    def create(self, request, *args, **kwargs):
        user = request.user
        inviteCode = GenerateInviteCode()
        myPlayerName = Player.objects.get(alias=user.username)
        Game.objects.create(
            playerX=myPlayerName,
            xState = 'joined',
            inviteCode = inviteCode
        )

        return Response({
                'message': 'game created',
                'invite_code': inviteCode
            }, status.HTTP_201_CREATED)

class JoinGameView(viewsets.ModelViewSet):
    serializer_class = JoinGameSerializer
    permission_classes = [permissions.IsAuthenticated]

    #this is not working. it should update game model and make it ready to start the game. 
    def create(self, request, *args, **kwargs):

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        user = request.user
        inviteCode = request.data.get('inviteCode')
        myPlayerName = Player.objects.get(alias=user.username)
        
        return Response({
            'message': 'you joined the game: ' + inviteCode
        }, status.HTTP_200_OK)
