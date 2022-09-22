"""URL configuration of the 'yatube_api' application."""

from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from django.views.generic import TemplateView

from yatube_api import settings

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include("api.urls")),
    path(
        "redoc/",
        TemplateView.as_view(template_name="redoc.html"),
        name="redoc",
    ),
]
if settings.DEBUG:
    urlpatterns += (
        path("api-auth/", include("rest_framework.urls")),
        path("__debug__/", include("debug_toolbar.urls")),
    )
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )
