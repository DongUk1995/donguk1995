from django.urls import path
from . import views

urlpatterns = [
    path("", views.tweeters),
    path("users/<int:pk>/tweets", views.tweeter),
]
