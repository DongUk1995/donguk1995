from ast import Pass
from django.contrib import admin
from .models import Room, Amenity


@admin.action(description="Set all prices to zero")
def rest_prices(model_admin, request, rooms):  # 3개 메서드는 필수
    for room in rooms.all():
        room.price = 0
        room.save()


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):

    actions = (rest_prices,)

    list_display = (
        "name",
        "price",
        "kind",
        "total_amenities",
        "rating",
        "owner",
        "created_at",
    )
    search_fields = ("^owner__username",)
    list_filter = (
        "country",
        "city",
        "pet_friendly",
        "kind",
        "amenities",
        "created_at",
        "updated_at",
    )


@admin.register(Amenity)
class AmenityAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "description",
        "created_at",
        "updated_at",
    )

    readonly_fields = (
        "created_at",
        "updated_at",
    )
