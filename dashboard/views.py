from django.shortcuts import render, redirect

from backend.models import *
from .forms import *

# -------------------------------- Display ----------------------------
def index(request):
    context = {}
    return render(request, "dashboard/index.html", context)




def activities(request):
    activities = Activity.objects.all()

    context = {"activities":activities}
    return render(request, "dashboard/items.html", context)




def images(request):
    images = Image.objects.all()
    context = {"images":images}
    return render(request, "dashboard/images.html", context)




# -------------------------------- Create ----------------------------
def createActivity(request):
    all_images = Image.objects.all()
    all_videos = Video.objects.all()
    message = ""

    if request.method == "POST":
        title = request.POST["title"]
        main_img = Image.objects.get(id=request.POST["main_img"])
        body = request.POST["body"]
        audio = request.POST["audio"]
        img_array = request.POST.getlist("img_array")
        vid_array = request.POST.getlist("vid_array")

        data = {"title":title,"main_img":main_img,"body":body,"audio":audio,"img_array":img_array,"vid_array":vid_array}

        form = ActivityForm(data)

        if form.is_valid():
            form.save()
            return redirect("dashboard:activities")
        else:
            message = "الرجاء ملئ جميع الحقول المطلوبة"

    context = {"message":message,"all_images":all_images, "all_videos":all_videos}
    return render(request, "dashboard/forms/create_form.html", context)




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
    all_images = Image.objects.all()
    all_videos = Video.objects.all()
    message = ""

    activity = Activity.objects.get(id=pk)
    form = ActivityForm(instance=activity)
    title = activity.title
    main_img = activity.main_img
    audio = activity.audio
    body = activity.body
    img_array = activity.img_array.all
    vid_array = activity.vid_array.all

    data = {"title":title,"main_img":main_img,"audio":audio,"body":body,"img_array":img_array,"vid_array":vid_array}

    if request.method == "POST":
        form = ActivityForm(request.POST, instance=activity)
        if form.is_valid():
            form.save()
            return redirect("dashboard:activities")
        else:
            message = "Form is not valid"

    context = {"message":message,"all_images":all_images,"all_videos":all_videos,"data":data}
    return render(request, "dashboard/forms/create_form.html", context)




# -------------------------------- Delete ----------------------------
def deleteActivity(request, pk):
    activity = Activity.objects.get(id=pk)

    if request.method == "POST":
        activity.delete()
        return redirect("dashboard:activities")

    context = {"item":activity}
    return render(request, "dashboard/delete.html", context)