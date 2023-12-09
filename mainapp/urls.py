from django.urls import path
from . import views

app_name = "mainapp"

urlpatterns = [
    path("categories/", views.CategoryListView.as_view(), name="categories"),
    path("categories/<id>/puzzles/", views.PuzzleListView.as_view(), name="puzzles"),
]