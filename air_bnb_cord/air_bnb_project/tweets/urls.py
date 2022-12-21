from django.urls import path
from . import views

urlpatterns = [
    path("", views.Tweet_main.as_view()),
]
