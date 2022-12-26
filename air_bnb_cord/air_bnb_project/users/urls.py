from django.urls import path
from .views import user_impo, user_impose

urlpatterns = [
    path("", user_impo.as_view()),
    path("<int:pk>/", user_impose.as_view()),
]
