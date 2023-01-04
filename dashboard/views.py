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
    all_images = Image.objects.all()
    all_videos = Video.objects.all()
    message = ""

    if request.method == "POST":
        title = request.POST["title"]
        init_main_img = request.POST["main_img"]
        body = request.POST["body"]
        audio = request.POST["audio"]
        img_array = request.POST.getlist("img_array")
        vid_array = request.POST.getlist("vid_array")

        if(title != "" and init_main_img != "" and body != ""):
            main_img = Image.objects.get(id=init_main_img)
            instance = Activity.objects.create(title=title,main_img=main_img,audio=audio,body=body)
            instance.img_array.set(img_array)
            instance.vid_array.set(vid_array)
            message = "تم"
        else:
            message = "الرجاء ملئ جميع الحقول المطلوبة"

    context = {"message":message,"all_images":all_images, "all_videos":all_videos}
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
    # image = Image.objects.get(id=form.main_img.value)

    print(data)

    if request.method == "POST":
        form = ActivityForm(request.POST, instance=activity)
        if form.is_valid():
            form.save()
            return redirect("dashboard:activities")
        else:
            message = "Form is not valid"
    context = {"message":message,"all_images":all_images,"data":data}
    return render(request, "dashboard/activity_form.html", context)