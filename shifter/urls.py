from django.urls import path
from .views import UserView, TeamView, ShiftsView

urlpatterns = [
    path("user/", UserView.as_view()),
    path("team/", TeamView.as_view()),
    path("shifts/<id:str>", TeamView.as_view()),
]
