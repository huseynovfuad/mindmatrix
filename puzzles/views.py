from rest_framework import generics
from .models import Puzzle, PuzzleImage
from .serializers import PuzzleSerializer


class PuzzleView(generics.RetrieveAPIView):
    serializer_class = PuzzleSerializer

    def get_object(self):
        return Puzzle.objects.order_by("?").first()



from django.shortcuts import render
def puzzle_view(request, id):
    puzzle = Puzzle.objects.get(id=id)
    context = {"puzzle": puzzle}
    return render(request, "index.html", context)