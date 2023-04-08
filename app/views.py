from rest_framework import viewsets
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated

from app.models import User, Post, Comment
from app.permissions import ReaderAccessPermission
from app.serializers import UserSerializer, PostSerializer, CommentSerializer


# class UserCreateView(CreateAPIView):
#     model = User
#     serializer_class = UserCreateSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    default_permission = [AllowAny()]

    permissions = {
        'list': [ReaderAccessPermission()],
        'update': [IsAdminUser(), IsAuthenticated()],
        'destroy': [IsAdminUser()],
    }

    def get_permissions(self):
        return self.permissions.get(self.action, self.default_permission)


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    default_permission = [AllowAny()]

    permissions = {
        'create': [IsAuthenticated()],
        'list': [AllowAny()],
        'update': [IsAdminUser(), IsAuthenticated()],
        'destroy': [IsAdminUser(), IsAuthenticated()],
    }

    def get_permissions(self):
        return self.permissions.get(self.action, self.default_permission)


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    default_permission = [AllowAny()]

    permissions = {
        'create': [IsAuthenticated()],
        'list': [AllowAny()],
        'update': [IsAdminUser(), IsAuthenticated()],
        'destroy': [IsAdminUser(), IsAuthenticated()],
    }

    def get_permissions(self):
        return self.permissions.get(self.action, self.default_permission)

