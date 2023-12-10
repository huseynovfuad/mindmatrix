from django.urls import path
from . import views

app_name = "puzzles"

urlpatterns = [
    path("detail/<id>/", views.puzzle_detail_view, name="detail"),
    path("check/", views.PuzzleCheckView.as_view(), name="check"),
    path("submit/", views.PuzzleSubmitView.as_view(), name="submit"),
]