from django.urls import path
from . import views

app_name = "puzzles"

urlpatterns = [
    path("detail/<id>/", views.puzzle_view, name="index"),
    path("get/", views.PuzzleView.as_view(), name="get-puzzle"),
]