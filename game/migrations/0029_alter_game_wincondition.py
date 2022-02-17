# Generated by Django 3.2.8 on 2022-02-17 10:27

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0028_alter_game_wincondition'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='winCondition',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.PositiveIntegerField(), default=[-1, -1, -1], size=None),
        ),
    ]
