from rest_framework import viewsets, permissions, status
from .models import Player, Game
from .serializers import CreateGameSerializer
from rest_framework.response import Response

# Create your views here.

class CreateGameView(viewsets.ModelViewSet):
    serializer_class = CreateGameSerializer
    permission_classes = [permissions.IsAuthenticated]

    def create(self, request, *args, **kwargs):
        return Response({
                'message': 'here i am',
                'error': 'user_not_found'
            }, status.HTTP_404_NOT_FOUND)
