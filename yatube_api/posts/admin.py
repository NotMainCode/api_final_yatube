"""Admin site settings of the 'Posts' application."""

from django.contrib import admin

from .models import Comment, Follow, Group, Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    """Table settings for users posts on the admin site."""

    list_display = (
        "pk",
        "pub_date",
        "text",
        "author",
        "group",
    )
    list_editable = ("group",)
    search_fields = ("text",)
    list_filter = ("pub_date", "author", "group")
    empty_value_display = "-пусто-"


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    """Table settings for comments of posts on the admin site."""

    list_display = (
        "pk",
        "created",
        "author",
        "text",
        "post_id",
    )
    search_fields = ("author__username", "post__id")
    list_filter = ("author",)


@admin.register(Follow)
class FollowAdmin(admin.ModelAdmin):
    """Table settings for users subscriptions on the admin site."""

    list_display = (
        "pk",
        "user",
        "following",
    )
    list_filter = ("user", "following")


admin.site.register(Group)
