from django.shortcuts import render, redirect

from backend.models import *
from .forms import *

# -------------------------------- Read ----------------------------
def index(request):
    context = {}
    return render(request, "dashboard/index.html", context)




def activities(request):
    activities = Activity.objects.all()
    section = {
        "activities":True
    }

    context = {"items":activities,"section":section}
    return render(request, "dashboard/items.html", context)


def productions(request):
    productions = Production.objects.all()
    section = {
        "productions":True
    }

    context = {"items":productions,"section":section}
    return render(request, "dashboard/items.html", context)


def images(request):
    images = Image.objects.all()
    section = {
        "images":True
    }

    context = {"items":images,"section":section}
    return render(request, "dashboard/files.html", context)




# -------------------------------- Create ----------------------------
def createActivity(request):
    all_images = Image.objects.all()
    all_videos = Video.objects.all()
    message = ""
    section = {"max":True}

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

    context = {"section":section,"message":message,"all_images":all_images, "all_videos":all_videos}
    return render(request, "dashboard/forms/create_form.html", context)


def createProduction(request):
    all_images = Image.objects.all()
    message = ""
    section = {"book":True}

    if request.method == "POST":
        title = request.POST["title"]
        main_img = Image.objects.get(id=request.POST["main_img"])
        body = request.POST["body"]
        pdf_file = request.POST["pdf_file"]
        doc_file = request.POST["doc_file"]

        data = {"title":title,"main_img":main_img,"body":body,"pdf_file":pdf_file,"doc_file":doc_file}

        form = ProductionForm(data)

        if form.is_valid():
            form.save()
            return redirect("dashboard:productions")
        else:
            message = "الرجاء ملئ جميع الحقول المطلوبة"

    context = {"section":section,"message":message,"all_images":all_images}
    return render(request, "dashboard/forms/create_form.html", context)




def createImage(request):
    options = {
        "image":True,
        "multiple":True
    }

    if request.method == "POST":
        images = request.FILES.getlist("images")

        for image in images:
            Image.objects.create(image=image)

        return redirect("dashboard:images")
        

    context = {"options":options}
    return render(request, "dashboard/forms/upload_form.html", context)




def createVideo(request):
    options = {
        "video":True,
        "multiple":False
    }

    if request.method == "POST":
        vid_id = request.POST["vid_id"]
        title = request.POST["title"]

        Video.objects.create(vid_id=vid_id,title=title)

    context = {"options":options}
    return render(request, "dashboard/forms/upload_form.html", context)




def createAudio(request):
    options = {
        "audio":True,
        "multiple":False
    }

    if request.method == "POST":
        audio = request.FILES["audio"]
        title = request.POST["title"]

        Audio.objects.create(audio=audio,title=title)

    context = {"options":options}
    return render(request, "dashboard/forms/upload_form.html", context)




# -------------------------------- Update ----------------------------
def updateActivity(request, pk):
    section = {"max":True}
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

    context = {"section":section,"message":message,"all_images":all_images,"all_videos":all_videos,"data":data}
    return render(request, "dashboard/forms/create_form.html", context)


def updateProduction(request, pk):
    all_images = Image.objects.all()
    message = ""

    production = Production.objects.get(id=pk)
    form = ProductionForm(instance=production)
    title = production.title
    main_img = production.main_img
    body = production.body

    data = {"title":title,"main_img":main_img,"body":body}

    if request.method == "POST":
        form = ProductionForm(request.POST, instance=production)
        if form.is_valid():
            form.save()
            return redirect("dashboard:productions")
        else:
            message = "Form is not valid"

    context = {"message":message,"all_images":all_images,"data":data}
    return render(request, "dashboard/forms/create_form.html", context)




# -------------------------------- Delete ----------------------------
def deleteActivity(request, pk):
    activity = Activity.objects.get(id=pk)

    if request.method == "POST":
        activity.delete()
        return redirect("dashboard:activities")

    context = {"item":activity}
    return render(request, "dashboard/forms/delete_form.html", context)


def deleteProduction(request, pk):
    production = Production.objects.get(id=pk)

    if request.method == "POST":
        production.delete()
        return redirect("dashboard:productions")

    context = {"item":production}
    return render(request, "dashboard/forms/delete_form.html", context)

def deleteImage(request, pk):
    image = Image.objects.get(id=pk)
    image.delete()
    return redirect("dashboard:images")