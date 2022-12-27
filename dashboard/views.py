from django.shortcuts import render, redirect

from backend.models import *
from .forms import *

# Create your views here.
def activities(request):
    activities = Activity.objects.all()

    context = {"activities":activities}
    return render(request, "dashboard/activities.html", context)


def createActivity(request):
    form = ActivityForm()

    if request.method == "POST":
        form = ActivityForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("activities")

    context = {"form":form}
    return render(request, "dashboard/activity_form.html", context)


def updateActivity(request, pk):
    activity = Activity.objects.get(id=pk)
    form = ActivityForm(instance=activity)

    if request.method == "POST":
        form = ActivityForm(request.POST, instance=activity)
        if form.is_valid():
            form.save()
            return redirect("activities")

    context = {"form":form}
    return render(request, "dashboard/activity_form.html", context)