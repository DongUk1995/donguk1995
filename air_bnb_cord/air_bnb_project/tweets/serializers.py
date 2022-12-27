from rest_framework import serializers
from users.serializers import TinySerializer
from .models import Tweet, Like


class TweetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tweet
        fields = "__all__"


class TinyUserSerializer(serializers.ModelSerializer):
    user = TinySerializer(
        read_only=True,
    )

    class Meta:
        model = Like
        fields = (
            "user",
            "twitter",
        )


class TweetDetail(serializers.ModelSerializer):
    user = TinySerializer(read_only=True)
    user_tweet = TinyUserSerializer(read_only=True)

    class Meta:
        model = Tweet
        fields = "__all__"

    def get_is_owner(self, Tweet):
        request = self.context["request"]
        return Tweet.owner == request.user
