from django.db import models

# Create your models here.


class Player(models.Model):
    alias = models.CharField(max_length=256)

    def __str__(self):
        return self.alias