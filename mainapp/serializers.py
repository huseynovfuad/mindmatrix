from rest_framework import serializers
from .models import Category
from puzzles.models import PuzzleResult, Puzzle
from puzzles.serializers import PuzzleSerializer

class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        # fields = "__all__"
        exclude = ("order", )

    def to_representation(self, instance):
        repr_ = super().to_representation(instance)
        user = self.context.get("user")
        repr_["locked"] = not PuzzleResult.objects.filter(
            puzzle__category__order=instance.order-1, is_ok=True, user=user
        ).count() == instance.puzzle_set.count() if instance.order > 1 else False
        return repr_




class CategoryDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        exclude = ("order",)

    def to_representation(self, instance):
        repr_ = super().to_representation(instance)
        queryset = Puzzle.objects.filter(category=instance).order_by("order")
        repr_["puzzles"] = PuzzleSerializer(queryset, many=True, context=self.context).data
        return repr_