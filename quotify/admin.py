from django.contrib import admin

from .models import Quote, Author, Category, MonthlyQuoteList

class AuthorFilter(admin.SimpleListFilter):
    title = 'Author'
    parameter_name = 'author'

    def lookups(self, request, model_admin):
        authors = Author.objects.values_list('id', 'name')
        return tuple(authors)

    def queryset(self, request, queryset):
        value = self.value()
        if value:
            return queryset.filter(author__id=value)
        return queryset

class CategoryFilter(admin.SimpleListFilter):
    title = 'Category'
    parameter_name = 'category'

    def lookups(self, request, model_admin):
        categories = Category.objects.values_list('id', 'name')
        return tuple(categories)

    def queryset(self, request, queryset):
        value = self.value()
        if value:
            return queryset.filter(categories__id=value)
        return queryset

class QuoteAdmin(admin.ModelAdmin):
    list_display = ('text', 'author', 'display_categories')
    search_fields = ('text', 'author__name', 'categories__name')
    list_per_page = 50
    filter_horizontal = ('categories',)

    def display_categories(self, obj):
        return ", ".join([category.name for category in obj.categories.all()])

    display_categories.short_description = 'Categories'

admin.site.register(Quote, QuoteAdmin)

admin.site.register(Author)
admin.site.register(Category)


admin.site.register(MonthlyQuoteList)