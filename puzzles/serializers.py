from rest_framework import serializers
from .models import Puzzle, PuzzleImage


class PuzzleImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PuzzleImage
        fields = ("id", "image", )


class PuzzleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Puzzle
        fields = ("id", "title")


    def to_representation(self, instance):
        repr_ = super().to_representation(instance)
        repr_["images"] = PuzzleImageSerializer(
            PuzzleImage.objects.filter(puzzle=instance).order_by("?"), many=True
        ).data
        return repr_