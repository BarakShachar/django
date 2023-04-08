from django.urls import path
from .views import UserView, TeamView

urlpatterns = [
    path("user/", UserView.as_view()),
    path("team/", TeamView.as_view()),
]