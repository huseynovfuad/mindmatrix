from rest_framework import generics
from .serializers import PuzzleCheckSerializer
from .models import Puzzle, PuzzleImage, PuzzleResult
from rest_framework.response import Response


class PuzzleCheckView(generics.CreateAPIView):
    queryset = PuzzleResult.objects.all()
    serializer_class = PuzzleCheckSerializer

    def post(self, request, *args, **kwargs):
        result = request.data.get("result")
        serializer = self.serializer_class(data=request.data, context={"result": result})
        serializer.is_valid(raise_exception=True)
        return Response({"is_ok": True}, status=201)


class PuzzleSubmitView(generics.CreateAPIView):
    queryset = PuzzleResult.objects.all()
    serializer_class = PuzzleCheckSerializer

    def post(self, request, *args, **kwargs):
        result = request.data.get("result")
        serializer = self.serializer_class(data=request.data, context={"result": result, "user": request.user})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"is_ok": True}, status=201)


from django.shortcuts import render
def puzzle_detail_view(request, id):
    puzzle = Puzzle.objects.get(id=id)
    images = [(index+1, pzimage) for index, pzimage in enumerate(puzzle.puzzleimage_set.all())]
    context = {"images": images, "row": range(puzzle.row), "column": range(puzzle.column)}
    return render(request, "index.html", context)