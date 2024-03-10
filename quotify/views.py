import calendar
from random import sample
import string
from django.http import Http404 
from django.utils import timezone
from django.shortcuts import get_object_or_404, render, get_list_or_404
from quotify.models import Author, Category, MonthlyQuoteList, Quote
from django.core.paginator import Paginator
from django.db.models import Q


def home_view(request):
    return render(request, "quotify/home.html")


def todays_quote(request):
    today = timezone.now()

    monthly_quote_list, created = MonthlyQuoteList.objects.get_or_create(
        month=today.month,
        year=today.year,
    )
    if created:
        days_in_month = calendar.monthrange(today.year, today.month)[1]
        quotes_for_month = Quote.objects.order_by("?")[:days_in_month]

        quotes_values = list(quotes_for_month.values())
        monthly_quote_list.quotes = quotes_values
        monthly_quote_list.save()
        quote = quotes_values[today.day]
        text = quote["text"]
        author = Author.objects.get(id=quote["author_id"])
        context = {"quote": text, "author": author}
    else:
        quotes_monthly = monthly_quote_list.quotes
        quote = quotes_monthly[today.day]
        text = quote["text"]
        author = Author.objects.get(id=quote["author_id"])
        context = {"quote": text, "author": author}
    return render(request, "quotify/todays_quote.html", context)


def authors_main_view(request):
    all_author_ids = Author.objects.values_list("id", flat=True)

    # Выбрать случайные 20 идентификаторов из списка
    random_author_ids = sample(list(all_author_ids), 20)

    # Получить авторов по выбранным идентификаторам
    random_authors = Author.objects.filter(id__in=random_author_ids).order_by("name")

    english_alphabet_upper = string.ascii_uppercase
    context = {"random_authors": random_authors, "abc": english_alphabet_upper}
    return render(request, "quotify/authors_main.html", context)


def authors_sort_letter(request, pk):
    if len(pk) == 1:
        authors_letter = Author.objects.filter(name__startswith=pk).order_by("name")
        english_alphabet_upper = string.ascii_uppercase

        pagination = Paginator(authors_letter, 30)
        page = request.GET.get("page")
        authors = pagination.get_page(page)

        context = {"authors": authors, "letter": pk, "abc": english_alphabet_upper}
        return render(request, "quotify/authors_letter.html", context)
    else:
        raise Http404


def authors_page(request, slug_author):
    author = get_object_or_404(Author, slug=slug_author)
    quotes_list = get_list_or_404(Quote, author=author)
    pagination = Paginator(quotes_list, 20)
    page = request.GET.get("page")
    quotes = pagination.get_page(page)

    return render(
        request, "quotify/authors_page.html", {"quotes": quotes, "author": author}
    )


def list_categories(request):
    categories = Category.objects.all().order_by("name")
    return render(request, "quotify/categories.html", {"categories": categories})


def category_page(request, slug_category):
    category = get_object_or_404(Category, slug=slug_category)
    quotes_in_category = Quote.objects.filter(categories=category)
    pagination = Paginator(quotes_in_category, 20)
    page = request.GET.get("page")
    quotes = pagination.get_page(page)
    context = {"category": category, "quotes": quotes}

    return render(request, "quotify/categories_page.html", context)


def search_quote(request):
    searchTerm = request.GET.get("searchTerm", "")

    if searchTerm:
        result = Quote.objects.filter(
            Q(text__icontains=searchTerm) | Q(author__name__icontains=searchTerm)
        ).order_by("id")
        pagination = Paginator(result, 20)
        page = request.GET.get("page")
        quotes = pagination.get_page(page)

        return render(
            request,
            "quotify/search_quote.html",
            {"searched": searchTerm, "quotes": quotes},
        )
    else:
        return render(request, "quotify/search_quote.html")
