from django.contrib.sitemaps import Sitemap
from django.shortcuts import resolve_url

from camera.models import Camera
from ranking.models import Rank


class CameraSitemap(Sitemap):
    changefreq = "monthly"

    def items(self):
        return Camera.objects.all()

    def location(self, obj):
        return resolve_url('camera:detail', camera_id=obj.pk)

    def lastmod(self, obj):
        return obj.updated_at


class RankSitemap(Sitemap):
    changefreq = "weekly"

    def items(self):
        return Rank.objects.all()

    def location(self, obj):
        return resolve_url('ranking:detail', pk=obj.pk, sort_type="review")

    def lastmod(self, obj):
        return obj.updated_at


class StaticSitemap(Sitemap):
    changefreq = "never"

    def items(self):
        return ["camera:top_page", "camera:search", "ranking:index"]

    def location(self, obj):
        return resolve_url(obj)
