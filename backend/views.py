from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Q

from .models import *

# Create your views here
def home(request):
    activities = Activity.objects.all().exclude(active=False)[:5]
    productions =  Production.objects.all().exclude(active=False)

    context = {"activities":activities,"productions":productions}
    return render(request, "backend/home.html", context)


def page_items(request, slug):
    page = Page.objects.get(slug=slug)
    items = page.articles.all()

    context = {"items":items, "page": page}
    return render(request, "backend/section.html", context)

def item_details(request, slug, pk):
    page = Page.objects.get(slug=slug)
    item = page.articles.get(id=pk)

    context = {"item": item, "page": page}
    return render(request, "backend/article.html", context)


# Section views
def activities(request):
    activities = Activity.objects.all().exclude(active=False)

    context = {"activities":activities}
    return render(request, "backend/section.html", context)


def productions(request):
    productions =  Production.objects.all().exclude(active=False)

    context = {"productions":productions}
    return render(request, "backend/section.html", context)




# Article views
def activity(request, pk):
    activity = Activity.objects.get(id=pk)
    section = {"activities":"activities"}
    context = {"item":activity,"section":section}

    return render (request, "backend/article.html", context)


def production(request, pk):
    production = Production.objects.get(id=pk)
    section = {"productions":"productions","book":True}
    context = {"item":production,"section":section}

    return render (request, "backend/article.html", context)


def pBooks(request):
    pBooks = pBook.objects.all()
    section = {"activities":"activities"}
    context = {"pBooks":pBooks}
    return render(request, "backend/library.html", context)


@csrf_exempt
def searchLibrary(request):
    search_term = request.GET.get("q")
    search_field = request.GET.get("field")
    if search_field == "all":
        books = pBook.objects.filter(Q(title__icontains=search_term) | Q(author__icontains=search_term) | Q(translator__icontains=search_term) | Q(investigator__icontains=search_term) | Q(publisher__icontains=search_term) | Q(edition__icontains=search_term) | Q(pdate__icontains=search_term) | Q(description__icontains=search_term) | Q(century__icontains=search_term) | Q(language__icontains=search_term) | Q(phouse__icontains=search_term) | Q(size__icontains=search_term) | Q(crate__icontains=search_term) | Q(shelf__icontains=search_term))
    elif search_field == "title":
        books = pBook.objects.filter(title__icontains=search_term)
    elif search_field == "person":
        books = pBook.objects.filter(Q(author__icontains=search_term) | Q(translator__icontains=search_term) | Q(investigator__icontains=search_term))
    elif search_field == "publisher":
        books = pBook.objects.filter(publisher__icontains=search_term)
    elif search_field == "edition":
        books = pBook.objects.filter(edition__icontains=search_term)
    elif search_field == "pdate":
        books = pBook.objects.filter(pdate__icontains=search_term)
    elif search_field == "description":
        books = pBook.objects.filter(description__icontains=search_term)
    elif search_field == "century":
        books = pBook.objects.filter(century__icontains=search_term)
    elif search_field == "language":
        books = pBook.objects.filter(language__icontains=search_term)
    elif search_field == "phouse":
        books = pBook.objects.filter(phouse__icontains=search_term)
    elif search_field == "size":
        books = pBook.objects.filter(size__icontains=search_term)
    elif search_field == "crate":
        books = pBook.objects.filter(crate__icontains=search_term)
    elif search_field == "shelf":
        books = pBook.objects.filter(shelf__icontains=search_term)
    else:
        books = pBook.objects.none()
    data = {"books": list(books.values())}
    return JsonResponse(data, safe=False)