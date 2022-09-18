"""URLs request handlers of the 'api' application."""

from django.shortcuts import get_object_or_404
from rest_framework import filters, viewsets
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import IsAuthenticated

from api.permissions import IsAuthorOrReadOnly
from api.serializers import (
    CommentSerializer,
    FollowSerializer,
    GroupSerializer,
    PostSerializer,
)
from api.viewsets import CreateListViewSet
from posts.models import Group, Post


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.select_related("author")
    serializer_class = PostSerializer
    permission_classes = (IsAuthorOrReadOnly,)
    pagination_class = LimitOffsetPagination

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = (IsAuthorOrReadOnly,)

    def perform_create(self, serializer):
        post = get_object_or_404(Post, id=self.kwargs["post_pk"])
        author = self.request.user
        serializer.save(author=author, post=post)

    def get_queryset(self):
        post = get_object_or_404(Post, id=self.kwargs["post_pk"])
        return post.comments.select_related("author")


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class FollowViewSet(CreateListViewSet):
    serializer_class = FollowSerializer
    permission_classes = (IsAuthenticated,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ("following__username",)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        return self.request.user.follower.select_related("following")
