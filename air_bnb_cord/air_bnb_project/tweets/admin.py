from django.contrib import admin
from .models import Tweet, Like


class ElonMusk(admin.SimpleListFilter):
    title = "Tweet Filter!"
    parameter_name = "Elon"

    def lookups(self, request, model_admin):
        return [
            ("ElonMusk", "ElonMush search: YES"),
            ("donguk", "ElonMush search: NO"),
        ]

    def queryset(self, request, tweets):
        Elon = self.value()
        if Elon:
            return tweets.filter(payload__contains=Elon)
        else:
            return tweets


@admin.register(Tweet)
class TweetAdmin(admin.ModelAdmin):

    list_display = (
        "payload",
        "user",
        "total_likes",
        "created_at",
        "updated_ate",
    )

    search_fields = (
        "user__username",
        "payload",
    )
    list_filter = (
        ElonMusk,
        "created_at",
    )


@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "twitter",
        "created_at",
        "updated_ate",
    )
    search_fields = ("user__username",)
    list_filter = ("created_at",)
