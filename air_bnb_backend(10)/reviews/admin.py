from django.contrib import admin
from .models import Review


class RatingFilter(admin.SimpleListFilter):

    title = "점수별 리뷰 보기"

    parameter_name = "donguk"

    def lookups(self, request, model_admin):
        return [
            ("goodReview", "좋은리뷰(3점이상)"),
            ("badReview", "나쁜리뷰(3점이하)"),
        ]

    def queryset(self, request, reviews):
        donguk = self.value()
        if donguk == "badReview":
            return reviews.filter(rating__lt=3)
        elif donguk == "goodReview":
            return reviews.filter(rating__gte=3)
        else:
            return reviews


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):

    list_display = (
        "__str__",
        "payload",
    )

    list_filter = (
        RatingFilter,
        "rating",
        "user__is_host",
        "room__category",
        "room__pet_friendly",
    )
