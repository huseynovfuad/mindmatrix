from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Puzzle, PuzzleImage
from .utils import create_puzzle_pieces


# method for updating
@receiver(post_save, sender=Puzzle)
def update_stock(sender, instance, created, **kwargs):
    if not created:
        PuzzleImage.objects.filter(puzzle=instance).delete()

    create_puzzle_pieces(instance)