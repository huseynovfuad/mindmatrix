from rest_framework import serializers
from .models import Puzzle, PuzzleImage, PuzzleResult
from django.core.files.images import ImageFile


class PuzzleImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PuzzleImage
        fields = ("id", "image", )

    def to_representation(self, instance):
        repr_ = super().to_representation(instance)
        repr_["width"] = instance.image.width
        repr_["height"] = instance.image.height
        return repr_


class PuzzleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Puzzle
        fields = ("id", "title", "image",)


    def to_representation(self, instance):
        repr_ = super().to_representation(instance)
        repr_["images"] = PuzzleImageSerializer(
            PuzzleImage.objects.filter(puzzle=instance).order_by("?"), many=True
        ).data
        repr_["locked"] = False if instance.order == 1 else not PuzzleResult.objects.filter(
            puzzle__order=instance.order-1, is_ok=True, user=self.context.get("user")
        ).exists()
        return repr_




class PuzzleCheckSerializer(serializers.ModelSerializer):
    class Meta:
        model = PuzzleResult
        fields = ("id", "puzzle", "user", "is_ok")
        extra_kwargs = {
            "user": {"read_only": True},
            "is_ok": {"read_only": True},
        }


    def get_correct_list(self, id_list, row, column):
        data = []
        for i in range(row):
            data.append([id_list[i*row+j] for j in range(column)])
        return data


    def validate(self, attrs):
        puzzle = attrs.get("puzzle")
        id_list = PuzzleImage.objects.filter(puzzle=puzzle).order_by("id").values_list("id", flat=True)
        correct = self.get_correct_list(id_list, puzzle.row, puzzle.column)
        result = self.context.get("result")

        print(result)
        print(correct)
        print(type(result), type(correct))
        print(result == correct)
        if result != correct:
            raise serializers.ValidationError({"error": "Wrong ordering"})
        return attrs


    def create(self, validated_data):
        return PuzzleResult.objects.create(
            puzzle=validated_data.get("puzzle"), is_ok=True, user=self.context.get("user")
        )