from django.urls import path
from django.contrib.sitemaps.views import sitemap

from quotify_live.sitemaps import AuthorSitemap, CategorySitemap
from .views import (
    authors_page,
    authors_sort_letter,
    category_page,
    home_view,
    list_categories,
    todays_quote,
    authors_main_view,
    search_quote,
)
from django.views.generic import TemplateView


sitemaps = {"authors": AuthorSitemap, "category": CategorySitemap}


urlpatterns = [
    path("", home_view, name="home"),
    path("todays_quote/", todays_quote, name="todays_quote"),
    path("authors/", authors_main_view, name="authors"),
    path("authors/<str:pk>", authors_sort_letter, name="letters"),
    path("author/<slug:slug_author>", authors_page, name="authors_page"),
    path("categories/", list_categories, name="categories"),
    path("category/<slug:slug_category>", category_page, name="category"),
    path("search", search_quote, name="search_quote"),
    path(
        "robots.txt",
        TemplateView.as_view(
            template_name="quotify/robots.txt", content_type="text/plain"
        ),
        name="robots.txt",
    ),
    path(
        "ads.txt",
        TemplateView.as_view(
            template_name="quotify/ads.txt", content_type="text/plain"
        ),
        name="ads.txt",
    ),
    path(
        "sitemap.xml",
        sitemap,
        {"sitemaps": sitemaps},
        name="sitemap",
    ),
]
