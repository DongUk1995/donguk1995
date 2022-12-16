from django.db import models
from common.models import CommonModel


class Tweet(CommonModel):

    payload = models.TextField(
        max_length=180,
    )

    user = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
    )

    def __str__(self) -> str:
        return self.payload


class Like(CommonModel):
    user = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
    )

    twitter = models.ForeignKey(
        "tweets.Tweet",
        on_delete=models.CASCADE,
    )
