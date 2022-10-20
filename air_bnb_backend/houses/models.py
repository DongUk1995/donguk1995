from tabnanny import verbose
import django
from django.db import models


class House(models.Model):

    """model Definition for House"""

    name = models.CharField(max_length=140)
    price_per_night = models.PositiveBigIntegerField(
        verbose_name="Price", help_text="Positive Numbers Only"
    )
    description = models.TextField()
    address = models.CharField(max_length=140)
    pets_allowed = models.BooleanField(
        verbose_name="Pets Allowed?",
        default=True,
        help_text="DOes this house allow pets?",
    )
    owner = models.ForeignKey("users.User", on_delete=models.CASCADE)  ##데이터 타입

    def __str__(self):
        return self.name  ##str 메서드를 설정하는 것
