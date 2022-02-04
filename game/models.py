from asyncio.base_futures import _FINISHED
from django.db import models
from django.contrib.postgres.fields import ArrayField

# Create your models here.


class Player(models.Model):
    NOT_READY = 0
    JOINED = 1
    LEAVED = 2

    PLAYER_STATE = [
        (NOT_READY, 'NOT_READY'),
        (JOINED, 'JOINED'),
        (LEAVED, 'LEAVED'),
    ]

    alias = models.CharField(max_length=256)

    def __str__(self):
        return self.alias

class Game(models.Model):
    WAITING = 0
    READY = 1
    DELETED = 2
    FINISHED = 3

    PLAYER_X = 0
    PLAYER_O = 1

    DRAW = 3

    GAME_STATE = [
        (WAITING, 'WAITING'),
        (READY, 'READY'),
        (DELETED,'DELETED'),
        (FINISHED,'FINISHED'),
    ]

    PLAYERS = [
        (PLAYER_X, 'PLAYER_X'),
        (PLAYER_O, 'PLAYER_O'),
    ]

    WIN_OPTIONS  = [
        (PLAYER_X, 'X'),
        (PLAYER_O, 'O'),
        (DRAW, 'DRAW'),
    ]

    gameBoard = ArrayField(
         models.CharField(max_length=1),
         default=list([
            None, None, None,
            None, None, None,
            None, None, None
         ]),
        size=9
    )
    status = models.CharField(choices=GAME_STATE, max_length=32)
    playerX = models.ForeignKey(Player, related_name="games_created", on_delete=models.CASCADE, null=True)
    playerO = models.ForeignKey(Player, related_name="games_invited", on_delete=models.CASCADE, null=True)
    nextPlayer = models.CharField(choices=PLAYERS, max_length=1, default='X')
    xState =  models.CharField(choices=Player.PLAYER_STATE, max_length=16, default='NOT_READY')
    oState =  models.CharField(choices=Player.PLAYER_STATE, max_length=16, default='NOT_READY')
    winner = models.CharField(choices=WIN_OPTIONS, max_length=1, null=True)
    inviteCode = models.CharField(unique=True, max_length=10, null=True)

    def __str__(self):
        return str(self.playerX) + " And " + str(self.playerO)