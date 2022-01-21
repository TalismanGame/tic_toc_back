from ast import alias
from rest_framework import viewsets, permissions, status
from .models import Player, Game
from .serializers import CreateGameSerializer
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
