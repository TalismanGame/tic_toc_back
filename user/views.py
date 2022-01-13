from rest_framework import viewsets, permissions, status
from .models import MyUser
from game.models import Player
from .serializers import LoginSerializer, RegisterSerializer, UserSerializer
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate

class LoginView(viewsets.ModelViewSet):
    queryset = MyUser.objects.all()
    serializer_class = LoginSerializer
    permission_classes = [permissions.AllowAny]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        username = request.data.get('username')
        password = request.data.get('password')

        user = authenticate(
            request=request,
            username=username,
            password=password,
        )

        if not user:
            return Response({
                'message': 'user not found',
                'error': 'user_not_found'
            }, status.HTTP_404_NOT_FOUND)
        else:
            token = Token.objects.get(user=user)
            # token = Token.objects.get(username=username)
            return Response({"token": token.key, "user": UserSerializer(user).data}, status.HTTP_200_OK)

class RegisterView(viewsets.ModelViewSet):
    queryset = MyUser.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [permissions.AllowAny]

    def create(self, request, *args, **kwargs):
        password = request.data.get("password")
        username = request.data.get("username")
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=False)

        if MyUser.objects.filter(username=username).exists():
            return Response(
                {
                    "message": "username already exists.",
                    "error": "username_already_exist",
                },
                status=status.HTTP_400_BAD_REQUEST,
            )
        user = serializer.save()
        token = Token.objects.create(user=user)
        headers = self.get_success_headers(serializer.data)
        user.set_password(password)
        Player.objects.create(alias=username)
        user.save()

        return Response(
            {
                "token": token.key,
                "user": UserSerializer(user).data
            },
            status=status.HTTP_201_CREATED,
            headers=headers,
        )
