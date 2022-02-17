# Generated by Django 3.2.8 on 2022-02-15 22:28

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0027_game_wincondition'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='winCondition',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.PositiveIntegerField(), default=[0, 0, 0], size=None),
        ),
    ]