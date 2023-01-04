from django.shortcuts import render, redirect

from backend.models import *
# from .forms import *

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
    all_images = Image.objects.all()
    all_videos = Video.objects.all()

    if request.method == "POST":
        title = request.POST["title"]
        main_img = Image.objects.get(id=request.POST["main_img"])
        audio = request.POST["audio"]
        body = request.POST["body"]
        img_array = request.POST.getlist("img_array")
        vid_array = request.POST.getlist("vid_array")

        instance = Activity.objects.create(title=title,main_img=main_img,audio=audio,body=body)
        instance.img_array.set(img_array)
        instance.vid_array.set(vid_array)

    context = {"all_images":all_images, "all_videos":all_videos}
    return render(request, "dashboard/activity_form.html", context)




def createImage(request):
    if request.method == "POST":
        images = request.FILES.getlist("images")

        for image in images:
            Image.objects.create(image=image)

    context = {}
    return render(request, "dashboard/image_form.html", context)




def createVideo(request):
    if request.method == "POST":
        vid_id = request.POST["vid_id"]
        title = request.POST["title"]

        Video.objects.create(vid_id=vid_id,title=title)

    context = {}
    return render(request, "dashboard/video_form.html", context)




def createAudio(request):
    if request.method == "POST":
        audio = request.FILES["audio"]
        title = request.POST["title"]

        instance = Audio.objects.create(audio=audio,title=title)
        instance.save()
        updatedContext = {"audio":instance.audio.url,"title":instance.title}
        return render(request, "dashboard/audio_form.html", updatedContext)

    context = {}
    return render(request, "dashboard/audio_form.html", context)
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