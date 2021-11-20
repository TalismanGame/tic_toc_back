from rest_framework import serializers, viewsets, permissions, status
from .models import MyUser
from .serializers import LoginSerializer, RegisterSerializer
from rest_framework.response import Response
from rest_framework.authtoken.models import Token

# Create your views here.


class LoginView(viewsets.ModelViewSet):
    queryset = MyUser.objects.all()
    serializer_class = LoginSerializer
    permission_classes = [permissions.AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        headers = self.get_success_headers(serializer.data)
        return Response('sssss', status=status.HTTP_200_OK, headers=headers)


class RegisterView(viewsets.ModelViewSet):
    queryset = MyUser.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [permissions.AllowAny]

    def create(self, request, *args, **kwargs):
        print('1111111111111111111111111111111111')
        password = request.data.get("password")
        username = request.data.get("username")
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=False)
        print('sssssssssssss', MyUser.objects.filter(username=username))
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
        user.save()

        return Response(
            {
                "message": "done",
                "token is": token.key
            },
            status=status.HTTP_201_CREATED,
            headers=headers,
        )
