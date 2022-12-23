from django.urls import path
from .views import tweeters, tweeter

urlpatterns = [
    path("", tweeters.as_view()),
    path("users/<int:pk>/tweets", tweeter.as_view()),
]
