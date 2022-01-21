from django.contrib import admin
from .models import Player, Game

class PlayerAdmin(admin.ModelAdmin):
    list_display = ["id", "alias", ]
admin.site.register(Player, PlayerAdmin)


class GameAdmin(admin.ModelAdmin):
    list_display = ["playerX", "xState", "playerO", "oState", "status", "inviteCode"]
    search_fields = ['playerX__alias', "playerO__alias"]

admin.site.register(Game, GameAdmin)
