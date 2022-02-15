# Generated by Django 3.2.8 on 2022-02-15 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0025_alter_game_gameboard'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='winner',
            field=models.PositiveIntegerField(choices=[(0, 'PLAYER_X'), (1, 'PLAYER_O'), (3, 'DRAW'), (4, 'NOT_DISCLOSED')], default=4),
        ),
    ]
