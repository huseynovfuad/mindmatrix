from rest_framework import generics
from .models import Puzzle, PuzzleImage
from .serializers import PuzzleSerializer


class PuzzleView(generics.RetrieveAPIView):
    serializer_class = PuzzleSerializer

    def get_object(self):
        return Puzzle.objects.order_by("?").first()