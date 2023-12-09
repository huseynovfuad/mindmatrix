from rest_framework import serializers
from django.contrib.auth import get_user_model, authenticate
from rest_framework_simplejwt.tokens import RefreshToken

User = get_user_model()


class LoginSerializer(serializers.ModelSerializer):
    username = serializers.CharField(required=True)

    class Meta:
        model = User
        fields = ("username", "password")
        extra_kwargs = {
            "password": {"write_only": True}
        }

    def get_user(self, username, password):
        return authenticate(username=username, password=password)

    def validate(self, attrs):
        username = attrs.get("username")
        password = attrs.get("password")

        user = self.get_user(username=username, password=password)

        if not user:
            return serializers.ValidationError("Username or Password is wrong")

        if not user.is_active:
            return serializers.ValidationError("This account is not activated")

        return attrs

    def create(self, validated_data):
        return self.get_user(
            username=validated_data.get("username"),
            password=validated_data.get("password")
        )

    def to_representation(self, instance):
        repr_ = super().to_representation(instance)
        token = RefreshToken.for_user(instance)
        repr_["tokens"] = {"refresh": str(token), "access": str(token.access_token)}
        return repr_




class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("username", "password")
        extra_kwargs = {
            "password": {"write_only": True}
        }

    def validate(self, attrs):
        password = attrs.get("password")

        if len(password) < 6:
            return serializers.ValidationError("Password should contain 6 characters at least")

        return super().validate(attrs)

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user


    def to_representation(self, instance):
        repr_ = super().to_representation(instance)
        token = RefreshToken.for_user(instance)
        repr_["tokens"] = {"refresh": str(token), "access": str(token.access_token)}
        return repr_



class AvatarSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "username", "avatar", )
        extra_kwargs = {
            "username": {"read_only": True}
        }


    def create(self, validated_data):
        user = self.context.get("user")
        avatar = validated_data.get("avatar")

        user.avatar = avatar
        user.save()
        return user




class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "username", "avatar")