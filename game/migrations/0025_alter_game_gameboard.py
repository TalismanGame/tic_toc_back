# Generated by Django 3.2.8 on 2022-02-15 10:37

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0024_auto_20220215_1006'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='gameBoard',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.PositiveIntegerField(), default=[0, 0, 0, 0, 0, 0, 0, 0, 0], size=9),
        ),
    ]
