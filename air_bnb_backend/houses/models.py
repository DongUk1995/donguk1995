from django.db import models

class House(models.Model):
    
    """model Definition for House"""

    name = models.CharField(max_length=140)
    price_per_night = models.PositiveBigIntegerField()
    description = models.TextField()
    address = models.CharField(max_length=140)
    pets_allowed = models.BooleanField(default=True)