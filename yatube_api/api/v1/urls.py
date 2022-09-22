"""URLs configuration of the 'api' application."""

from django.urls import include, path
from rest_framework.routers import DefaultRouter

from api.v1.views import (
    CommentViewSet,
    FollowViewSet,
    GroupViewSet,
    PostViewSet,
)

app_name = "api"

router_v1 = DefaultRouter()

router_v1.register("posts", PostViewSet, basename="post")
router_v1.register(
    r"posts/(?P<post_pk>\d+)/comments", CommentViewSet, basename="comment"
)
router_v1.register("groups", GroupViewSet, basename="group")
router_v1.register("follow", FollowViewSet, basename="follow")

urlpatterns = [
    path("", include(router_v1.urls)),
    path("", include("djoser.urls.jwt")),
]
