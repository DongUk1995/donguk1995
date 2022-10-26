from django.contrib import admin
from .models import Photo, Video


@admin.register(Photo)
class PhotoAdim(admin.ModelAdmin):
    pass


@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    pass
