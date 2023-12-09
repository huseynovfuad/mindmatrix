from django.contrib import admin
from .models import Puzzle, PuzzleImage, PuzzleResult

# Register your models here.

class PuzzleAdmin(admin.ModelAdmin):
    list_display = ("title", "category")

admin.site.register(Puzzle, PuzzleAdmin)
admin.site.register(PuzzleImage)
admin.site.register(PuzzleResult)
