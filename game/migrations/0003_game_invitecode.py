# Generated by Django 3.2.8 on 2022-01-21 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0002_auto_20220121_1806'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='inviteCode',
            field=models.CharField(max_length=8, null=True, unique=True),
        ),
    ]