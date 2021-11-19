from rest_framework import viewsets, permissions
from .models import MyUser
from serializers import LoginSerializer

# Create your views here.


class Login(viewsets.ModelViewSet):
    queryset = MyUser.objects.all()
    serializer_class = LoginSerializer
    permission_classes = [permissions.AllowAny]


