from django.shortcuts import render
from django.http import HttpResponse
from .models import *

# Create your views here.
def home(request):
    activities = Activity.objects.all()[:5]

    context = {"activities":activities}
    return render(request, "backend/home.html", context)


def activities(request):
    activities = Activity.objects.all()

    context = {"activities":activities}
    return render(request, "backend/activities.html", context)


def activity(request, pk):
    activity = Activity.objects.get(id=pk)

    context = {"activity":activity}
    return render (request, "backend/activity.html", context)