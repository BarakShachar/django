from django.urls import path
from .views import UserView, TeamView, ShiftsView

urlpatterns = [
    path("user/", UserView.as_view()),
    path("team/", TeamView.as_view()),
    path("shifts/<str:team_id>/", ShiftsView.as_view()),
]
