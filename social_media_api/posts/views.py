from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, permissions
from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


from rest_framework import filters

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'content']

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

from rest_framework import generics
from .models import Post
from .serializers import PostSerializer
from accounts.models import CustomUser

class UserFeed(generics.ListAPIView):
    serializer_class = PostSerializer
    
    def get_queryset(self):
        current_user = self.request.user
        following_users = current_user.following.all()
        return Post.objects.filter(author__in=following_users.all()).order_by('-created_at')
        return Post.objects.filter(author__in=following_users).order_by

from rest_framework import generics, permissions
from rest_framework.response import Response
from .models import Post, Like
from notifications.models import Notification
from notifications.serializers import NotificationSerializer  # Create this serializer
from accounts.models import CustomUser
from django.contrib.contenttypes.models import ContentType 

class LikePost(generics.CreateAPIView):
    queryset = Like.objects.all()
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        post = Post.objects.get(pk=self.kwargs['pk'])  # Get the post
        serializer.save(user=self.request.user, post=post)  # Save the like

        # Create a notification
        Notification.objects.create(
            recipient=post.author,  # Notify the post author
            actor=self.request.user,
            verb='liked your post',
            target_content_type=ContentType.objects.get_for_model(Post),
            target_object_id=post.id
        )

class UnlikePost(generics.DestroyAPIView):
    queryset = Like.objects.all()
    permission_classes = [permissions.IsAuthenticated]

    def perform_destroy(self, instance):
        instance.delete()  # Remove the like
