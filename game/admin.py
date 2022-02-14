from django.contrib import admin
from .models import Player, Game


# can also use decorator to register instead of admin.site.register. both work the same way
# You can’t use this decorator if you have to reference your model admin class in its __init__() method, e.g. super(PersonAdmin, self).__init__(*args, **kwargs). You can use super().__init__(*args, **kwargs).
# https://docs.djangoproject.com/en/4.0/ref/contrib/admin/


@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    list_display = ["id", "alias", ]
# admin.site.register(Player, PlayerAdmin)

@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    #question why this fields get empty after i add choices to them
    list_display = ["playerX", "xState", "playerO", "oState", "status", "inviteCode"]
    search_fields = ['playerX__alias', "playerO__alias"]

# admin.site.register(Game, GameAdmin)
