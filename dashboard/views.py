from django.shortcuts import render, redirect

from backend.models import *
from .forms import *

# -------------------------------- Display ----------------------------
def activities(request):
    activities = Activity.objects.all()

    context = {"activities":activities}
    return render(request, "dashboard/activities.html", context)




def images(request):
    images = Image.objects.all()
    context = {"images":images}
    return render(request, "dashboard/images.html", context)




# -------------------------------- Create ----------------------------
def createActivity(request):
    form = ImageForm()
    all_images = Image.objects.all()

    if request.method == "POST":
        title = request.POST["title"]
        main_img = request.POST["main_img"]
        body = request.POST["body"]

        activity = Activity.objects.create(title=title,main_img=main_img,body=body)

    context = {"form":form, "all_images":all_images}
    return render(request, "dashboard/activity_form.html", context)




def createImage(request):
    form = ImageForm()

    if request.method == "POST":
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()

    context = {"form":form}
    return render(request, "dashboard/image_form.html", context)



# -------------------------------- Update ----------------------------
def updateActivity(request, pk):
    pass
    # activity = Activity.objects.get(id=pk)
    # form = ActivityForm(instance=activity)

    # if request.method == "POST":
    #     form = ActivityForm(request.POST, instance=activity)
    #     if form.is_valid():
    #         form.save()
    #         return redirect("activities")

    # context = {"form":form}
    # return render(request, "dashboard/activity_form.html", context)