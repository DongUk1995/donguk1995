from django.db import models
from email.policy import default
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    class GenderChoicees(models.TextChoices):
        MALE = ("male", "Male")  ##데이터베이스에 들어갈 value를 갖고 있고 관리자 페이지에서 보게되는 label를 갖고 있어
        FEMALE = ("female", "Female")

    class LanguageChoices(models.TextChoices):
        KR = ("kr", "Korean")
        EN = ("en", "English")

    class CurrenctChoices(models.TextChoices):
        WON = "won", "Korean Won"
        USD = "usd", "Dollar"

    first_name = models.CharField(
        max_length=150,
        editable=False,
    )
    last_name = models.CharField(
        max_length=150,
        editable=False,
    )
    avatar = models.ImageField(
        blank=True,
    )
    name = models.CharField(
        max_length=150,
        default="",
    )
    is_host = models.BooleanField(
        default=False,
    )
    gender = models.CharField(
        max_length=10,
        choices=GenderChoicees.choices,
    )
    language = models.CharField(
        max_length=2,
        choices=LanguageChoices.choices,
    )
    curreny = models.CharField(
        max_length=5,
        choices=CurrenctChoices.choices,
    )
