from ast import alias
from asyncore import write
from rest_framework import viewsets, permissions, status
from .models import Player, Game
from .serializers import CreateGameSerializer, JoinGameSerializer, GetGameDataSerializer, LeaveGameSerializer
from rest_framework.response import Response
from .utils import GenerateInviteCode
from django.shortcuts import get_object_or_404
from .echoes import echo_when_game_status_updated
from asgiref.sync import async_to_sync

# Create your views here.

class CreateGameView(viewsets.ModelViewSet):
    # *************** do I really need this serializer here? I am not using it *****************
    serializer_class = CreateGameSerializer
    permission_classes = [permissions.IsAuthenticated]

    def create(self, request, *args, **kwargs):
        user = request.user
        inviteCode = GenerateInviteCode()
        myPlayerName = Player.objects.get(alias=user.username)
        Game.objects.create(
            playerX=myPlayerName,
            xState = Player.JOINED,
            oState = Player.NOT_READY,
            inviteCode = inviteCode,
            status = Game.WAITING
        )

        return Response({
                'message': 'game created',
                'invite_code': inviteCode
            }, status.HTTP_201_CREATED)

class JoinGameView(viewsets.ModelViewSet):
    serializer_class = JoinGameSerializer
    permission_classes = [permissions.IsAuthenticated]
    #this is not working. it should update game model and make it ready to start the game. 
    # ********* the logic I have to use is witten on board! :) ********* #

    

    def update(self, request, *args, **kwargs):
        # ******** question?? why do write queryset. how it helps us???? *******
        # queryset = Game.objects.all()

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        user = request.user
        inviteCode = request.data.get('inviteCode')
        myPlayerName = Player.objects.get(alias=user.username)

        targetGame = get_object_or_404(Game, inviteCode=inviteCode)

        # ******** question?? there should be a way to handle this way find it *******
        # Game.objects.update(
        #     id = targetGame,
        #     playerO=myPlayerName,
        #     oState = 'joined',
        #     status = 'ready',
        # )
        targetGame.playerO = myPlayerName
        targetGame.oState = Player.JOINED
        targetGame.status = Game.READY
        
        targetGame.save()

        async_to_sync(echo_when_game_status_updated)(
            data={"code": inviteCode, "gameStatus": Game.READY}
        )
        # ******** question?? how to send game data in response??? *******
        return Response({
            'message': 'game started!',
            # 'data': targetGame.playerX
        }, status.HTTP_200_OK)

class LeaveGameView(viewsets.ModelViewSet):
    serializer_class = LeaveGameSerializer
    permission_classes = [permissions.IsAuthenticated]

    def update(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        inviteCode = request.data.get('inviteCode')
        myTurnInGame = request.data.get('myTurnInGame')
        targetGame = get_object_or_404(Game, inviteCode=inviteCode)
        
        if myTurnInGame == 'x':
            targetGame.xState = Player.LEAVED
            targetGame.status = Game.WAITING
        elif myTurnInGame == 'o':
            targetGame.oState = Player.LEAVED
            targetGame.status = Game.WAITING    
        targetGame.save()

        return Response({
            'message': 'you leave the game',
            # 'data': targetGame.playerX
        }, status.HTTP_200_OK)


class UpdateGameData(viewsets.ModelViewSet):
    # serializer_class = UpdateGameDataSerializer
    permission_classes = [permissions.IsAuthenticated]

    def update(self, request, *args, **kwargs):
        # serializer = self.get_serializer(data=request.data)
        # serializer.is_valid(raise_exception=True)

        inviteCode = request.data.get('code')
        board = request.data.get('board')
        nextPlayer = request.data.get('nextPlayer')
        winner = request.data.get('winner')
        winCondition = request.data.get('winCondition')
        gameStatus = request.data.get('gameStatus')
        targetGame = get_object_or_404(Game, inviteCode=inviteCode)
        targetGame.gameBoard = board
        targetGame.nextPlayer = nextPlayer
        targetGame.winner = winner
        targetGame.winCondition = winCondition
        targetGame.status = gameStatus
        targetGame.save()
        return Response({
            'message': 'game updated! as hell',
        }, status.HTTP_200_OK)


class GameStateView(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]

    def retrieve(self, request, *args, **kwargs):
        inviteCode = kwargs.get("code", None)
        targetGame = get_object_or_404(Game, inviteCode=inviteCode)

        return Response({
            "status": targetGame.status
        }, status.HTTP_200_OK)

class GetGameDataView(viewsets.ModelViewSet):
    serializer_class = GetGameDataSerializer
    permission_classes = [permissions.IsAuthenticated]

    def retrieve(self, request, *args, **kwargs):
        inviteCode = kwargs.get("code", None)
        targetGame = get_object_or_404(Game, inviteCode=inviteCode)
        serializer = self.get_serializer(targetGame)
        return Response(serializer.data, status=status.HTTP_200_OK)
        


