from django.urls import path
from . import views

app_name = "puzzles"

urlpatterns = [
    path("check/", views.PuzzleCheckView.as_view(), name="check"),
    path("submit/", views.PuzzleSubmitView.as_view(), name="submit"),
]