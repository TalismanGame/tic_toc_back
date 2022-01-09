from rest_framework import serializers
from .models import MyUser

class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=False)
    class Meta:
        model = MyUser
        fields = [
            "username",
            "email",
            "password",
        ]


class LoginSerializer(serializers.ModelSerializer):
    username = serializers.CharField(
        label=("username"), write_only=True
    )
    password = serializers.CharField(
        label=("password"),
        style={"input_type": "password"},
        trim_whitespace=False,
        write_only=True,
    )
    token = serializers.CharField(label=("Token"), read_only=True)

    class Meta:
        model = MyUser
        fields = ["username", "password", "token"]


class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = MyUser
        fields = ["username", "email"]
     