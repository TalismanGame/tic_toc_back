# Generated by Django 3.2.8 on 2022-01-21 18:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0004_alter_game_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='inviteCode',
            field=models.CharField(max_length=10, null=True, unique=True),
        ),
    ]