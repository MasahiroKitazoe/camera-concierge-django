from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.contrib.sitemaps.views import sitemap

from cam_ranks.sitemap import (
    CameraSitemap,
    RankSitemap,
    StaticSitemap,
)

sitemaps = {
    "cameras": CameraSitemap,
    "ranking": RankSitemap,
    "static": StaticSitemap,
}

urlpatterns = [
    path('', include('camera.urls')),
    path('ranking/', include('ranking.urls')),
    path('admin/', admin.site.urls),
    path("sitemap.xml/", sitemap, {"sitemaps": sitemaps}, name="sitemap"),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),

        # For django versions before 2.0:
        # url(r'^__debug__/', include(debug_toolbar.urls)),

    ] + urlpatterns
