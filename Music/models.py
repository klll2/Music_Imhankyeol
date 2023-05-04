from django.db import models
from django.utils import timezone
import datetime

Genre_CHOICES = (
    (0, 'Jazz'),
    (1, 'Classic'),
    (2, 'Pop'),
)


class Music(models.Model):
    music_name = models.CharField(max_length=50)
    music_brand = models.CharField(max_length=100)
    music_price = models.IntegerField(default=0)
    music_buy = models.DateTimeField(default=timezone.now)
    music_producer = models.CharField(max_length=50)
    music_quantity = models.PositiveIntegerField(default=0)
    music_genre = models.IntegerField(choices=Genre_CHOICES, default = 0)