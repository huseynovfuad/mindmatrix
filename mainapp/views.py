from rest_framework import generics
from .models import Category
from puzzles.models import Puzzle
from .serializers import CategorySerializer, CategoryDetailSerializer
from rest_framework.response import Response
from .permissions import CheckCategoryLock

# Create your views here.


class CategoryListView(generics.ListAPIView):
    queryset = Category.objects.all().order_by("order")
    serializer_class = CategorySerializer

    def get(self, *args, **kwargs):
        serializer = self.serializer_class(self.get_queryset(), many=True, context={"user": self.request.user})
        return Response(serializer.data, status=200)



class PuzzleListView(generics.RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryDetailSerializer
    additional_permissions = [CheckCategoryLock]
    lookup_field = "id"


    def get_permissions(self):
        permission_classes = (
            self.permission_classes + self.additional_permissions
        )
        return [permission() for permission in permission_classes]


    def get(self, *args, **kwargs):
        serializer = self.serializer_class(self.get_object(), context={"user": self.request.user})
        return Response(serializer.data, status=200)



