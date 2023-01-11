from django.shortcuts import render
from django.http import HttpResponse

from hitcount.utils import get_hitcount_model
from hitcount.views import HitCountMixin

from .models import *

# Create your views here
def home(request):
    activities = Activity.objects.all().exclude(active=False)[:5]
    productions =  Production.objects.all().exclude(active=False)

    context = {"activities":activities,"productions":productions}
    return render(request, "backend/home.html", context)


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

    # hitcount logic
    hit_count = get_hitcount_model().objects.get_for_object(activity)
    hits = hit_count.hits
    hitcontext = context['hitcount'] = {'pk': hit_count.pk}
    hit_count_response = HitCountMixin.hit_count(request, hit_count)
    if hit_count_response.hit_counted:
        hits = hits + 1
    hitcontext['hit_counted'] = hit_count_response.hit_counted
    hitcontext['hit_message'] = hit_count_response.hit_message
    hitcontext['total_hits'] = hits

    return render (request, "backend/article.html", context)


def production(request, pk):
    production = Production.objects.get(id=pk)
    section = {"productions":"productions","book":True}
    context = {"item":production,"section":section}

    # hitcount logic
    hit_count = get_hitcount_model().objects.get_for_object(production)
    hits = hit_count.hits
    hitcontext = context['hitcount'] = {'pk': hit_count.pk}
    hit_count_response = HitCountMixin.hit_count(request, hit_count)
    if hit_count_response.hit_counted:
        hits = hits + 1
    hitcontext['hit_counted'] = hit_count_response.hit_counted
    hitcontext['hit_message'] = hit_count_response.hit_message
    hitcontext['total_hits'] = hits

    return render (request, "backend/article.html", context)