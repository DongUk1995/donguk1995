from django.urls import path
from . import views

urlpatterns = [
    path("", views.tweeters.as_view()),
    path("<int:pk>/", views.tweeter.as_view()),
    path("user/<int:pk>/", views.User_pk.as_view()),
    path("user/<int:pk>/tweets/", views.User_tweets.as_view()),
]
