from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = (
    [
        path("", include("app.urls")),
        path("dash/",include("admin.urls")),
        path("dashboard/", include("dashboard.urls"))
    ]
    + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
)


if settings.DEBUG:
    import debug_toolbar

    urlpatterns.extend(
        (
            path("admin/", admin.site.urls),
            path("__debug__/", include(debug_toolbar.urls)),
        )
    )
