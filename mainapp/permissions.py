from rest_framework.permissions import BasePermission
from puzzles.models import PuzzleResult
import json


class CheckCategoryLock(BasePermission):
    message = "Playing this category, firstly you need finish previous category puzzles"

    def has_object_permission(self, request, view, obj):
        if obj.order == 1:
            return True

        if obj.order > 1:
            return PuzzleResult.objects.filter(
                user=request.user, puzzle__category__order=obj.order-1, is_ok=True
            ).count() == obj.puzzle_set.count()
