from rest_framework.routers import DefaultRouter
from .views import PostViewSet, CommentViewSet

router = DefaultRouter()
router.register('posts', PostViewSet)
router.register('comments', CommentViewSet)

urlpatterns = router.urls


from django.urls import path
from .views import UserFeed

urlpatterns = [
    path('feed/', UserFeed.as_view(), name='user_feed'),
]

from django.urls import path
from .views import LikePost, UnlikePost

urlpatterns = [
    path('posts/<int:pk>/like/', LikePost.as_view(), name='like-post'),
    path('posts/<int:pk>/unlike/', UnlikePost.as_view(), name='unlike-post'),
]
