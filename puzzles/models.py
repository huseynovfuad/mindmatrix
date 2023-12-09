from django.db import models
from django.utils.text import slugify

# Create your models here.


def upload_to_puzzles(instance, filename):
    return f"puzzles/{slugify(instance.title)}/{filename}"

class Puzzle(models.Model):
    title = models.CharField(max_length=400)
    image = models.ImageField(upload_to=upload_to_puzzles)
    row = models.PositiveIntegerField(default=5)
    column = models.PositiveIntegerField(default=5)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Puzzle"


def upload_to_puzzle_images(instance, filename):
    return f"puzzles/{slugify(instance.puzzle.title)}/images/{instance.row}-{instance.col}/{filename}"

class PuzzleImage(models.Model):
    puzzle = models.ForeignKey(Puzzle, on_delete=models.CASCADE)
    image = models.ImageField(upload_to=upload_to_puzzle_images, blank=True,null=True)
    row = models.IntegerField(blank=True, null=True)
    col = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.puzzle.title

    class Meta:
        verbose_name_plural = "Puzzle Images"
