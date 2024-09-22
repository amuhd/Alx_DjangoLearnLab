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
from django.shortcuts import get_object_or_404
from .models import Post, Like
from notifications.models import Notification
from accounts.models import CustomUser
from django.contrib.contenttypes.models import ContentType

class LikePost(generics.CreateAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pk, *args, **kwargs):
        post = get_object_or_404(Post, pk=pk)  # Retrieve the post
        like, created = Like.objects.get_or_create(user=request.user, post=post)  # Like or get existing

        if created:
            # Create a notification if a new like is created
            Notification.objects.create(
                recipient=post.author,
                actor=request.user,
                verb='liked your post',
                target_content_type=ContentType.objects.get_for_model(Post),
                target_object_id=post.id
            )
            return Response({"message": "Post liked."}, status=201)
        else:
            return Response({"message": "You already liked this post."}, status=400)

class UnlikePost(generics.DestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def delete(self, request, pk, *args, **kwargs):
        post = get_object_or_404(Post, pk=pk)  # Retrieve the post
        try:
            like = Like.objects.get(user=request.user, post=post)  # Find the like
            like.delete()  # Remove the like
            return Response({"message": "Post unliked."}, status=204)
        except Like.DoesNotExist:
            return Response({"message": "You have not liked this post."}, status=400)
