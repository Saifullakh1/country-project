from django.db import models


class Coke(models.Model):
    price = models.IntegerField(default=0)
    volume = models.FloatField(default=0)
    bottle = models.CharField(max_length=20)
    is_original = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.price} - {self.volume}"






