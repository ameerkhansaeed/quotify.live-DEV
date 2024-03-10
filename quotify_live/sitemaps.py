from django.contrib.sitemaps import Sitemap
from quotify.models import Category, Author


class AuthorSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.9

    def items(self):
        return Author.objects.all().order_by("name")

    def lastmod(self, obj):
        pass


class CategorySitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.9

    def items(self):
        return Category.objects.all().order_by("name")

    def lastmod(self, obj):
        pass
