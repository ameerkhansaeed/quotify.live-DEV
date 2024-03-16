from django.db import models
from django.urls import reverse
from django.utils.text import slugify


class Author(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=255, blank=True, db_index=True, default="", null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Authors"

    def get_absolute_url(self):
        return reverse("authors_page", kwargs={"slug_author": self.slug})

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Author, self).save(*args, **kwargs)


class Category(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=255, unique=True, db_index=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Categories"

    def get_absolute_url(self):
        return reverse("category", kwargs={"slug_category": self.slug})

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)


class Quote(models.Model):
    text = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    categories = models.ManyToManyField(Category)

    def __str__(self) -> str:
        return f"{self.text} - {self.author}"

    class Meta:
        indexes = [models.Index(fields=["text"])]
        ordering = ("author", )


class MonthlyQuoteList(models.Model):
    month = models.PositiveIntegerField()
    year = models.PositiveIntegerField()
    quotes = models.JSONField(blank=True, null=True)

    def __str__(self):
        return f"{self.month}/{self.year} Quote List"
