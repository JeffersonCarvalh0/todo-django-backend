from django.contrib.auth.models import User

from rest_framework import viewsets, generics
from rest_framework.permissions import BasePermission, IsAuthenticated, AllowAny

from .models import Todo
from .serializers import TodoSerializer, UserSerializer

class IsAuthorized(BasePermission):
    message = 'Unauthorized user'

    def has_object_permission(self, request, view, obj):
        if type(obj) is User:
            return obj == request.user

        return obj.created_by == request.user

class TodoViewSet(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    permission_classes = [IsAuthenticated, IsAuthorized]

    def get_queryset(self):
        return Todo.objects.filter(created_by=self.request.user)

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated, IsAuthorized]

class UserCreate(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

