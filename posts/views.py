from django.contrib.auth import get_user_model
from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser
from django_filters.rest_framework import *

from .models import Post
from .permissions import IsAuthorOrReadOnly
from .serializers import PostSerializer, UserSerializer


class PostViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class UserViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAdminUser]  # new
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['is_superuser', 'is_active']
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
