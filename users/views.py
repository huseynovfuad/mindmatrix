from rest_framework import generics
from django.contrib.auth import get_user_model
from .serializers import (
    LoginSerializer, RegisterSerializer, AvatarSerializer
)
from rest_framework.response import Response

User = get_user_model()


class LoginView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = LoginSerializer
    permission_classes = ()


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = ()



class UpdateAvatarView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = AvatarSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={"user": request.user})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=201)