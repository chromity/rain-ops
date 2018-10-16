from django.db import models
from datetime import datetime


class SensorData(models.Model):
    time = models.DateTimeField(auto_now_add=True)
    water_level = models.IntegerField()
    rain_audio_level = models.FloatField()
    is_raining = models.BooleanField()

    def __str__(self):
        return str(self.time)
