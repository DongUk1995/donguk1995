from django.db import models

class House(models.Model):
    
    """model Definition for House"""

    name = models.CharField(max_length=140)
    price = models.PositiveBigIntegerField()
    description = models.TextField()
    address = models.CharField(max_length=140)
