from django.db import models
from django.contrib.postgres.fields import ArrayField

# Create your models here.


class Player(models.Model):
    alias = models.CharField(max_length=256)

    def __str__(self):
        return self.alias

class Game(models.Model):
    gameBoard = ArrayField(
         models.CharField(max_length=1),
         default=list([
            None, None, None,
            None, None, None,
            None, None, None
         ]),
        size=9
    )
    status = models.CharField(max_length=32, null=True)
    playerX = models.ForeignKey(Player, related_name="x", on_delete=models.CASCADE, null=True)
    playerO = models.ForeignKey(Player, related_name="O", on_delete=models.CASCADE, null=True)
    nextPlayer = models.CharField(max_length=1, default='X')
    xState =  models.CharField(max_length=16, default='not_ready')
    oState =  models.CharField(max_length=16, default='not_ready')
    winner = models.CharField(max_length=1, null=True)

    def __str__(self):
        return "%s %s %s %s %s" % (
            self.tiles,
            self.state,
            self.playerNext,
            self.playerX,
            self.playerO
        )