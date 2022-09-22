"""Serializers of the 'api' application."""

from rest_framework import serializers
from rest_framework.relations import SlugRelatedField
from rest_framework.validators import UniqueTogetherValidator

from posts.models import Comment, Follow, Group, Post, User


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        fields = "__all__"
        model = Group


class PostSerializer(serializers.ModelSerializer):
    author = SlugRelatedField(slug_field="username", read_only=True)

    class Meta:
        fields = "__all__"
        model = Post


class CommentSerializer(serializers.ModelSerializer):
    author = SlugRelatedField(slug_field="username", read_only=True)

    class Meta:
        fields = "__all__"
        read_only_fields = ("post",)
        model = Comment


class FollowSerializer(serializers.ModelSerializer):
    user = SlugRelatedField(
        slug_field="username",
        read_only=True,
        default=serializers.CurrentUserDefault(),
    )
    following = SlugRelatedField(
        slug_field="username", queryset=User.objects.all()
    )

    class Meta:
        fields = (
            "user",
            "following",
        )
        model = Follow
        validators = [
            UniqueTogetherValidator(
                queryset=Follow.objects.all(),
                fields=("user", "following"),
                message="The subscription was created earlier.",
            )
        ]

    def validate_following(self, value):
        if self.context["request"].user == value:
            raise serializers.ValidationError(
                "Subscribing to yourself is not allowed."
            )
        return value
