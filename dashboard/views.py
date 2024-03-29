from django.shortcuts import render, redirect
from django.http import JsonResponse
import os

from backend.models import *
from .forms import *

class CustomManager(models.Manager):
    def delete(self):
        for obj in self.get_queryset():
            obj.delete()

# -------------------------------- Read ----------------------------
def index(request):
    context = {}
    return render(request, "dashboard/index.html", context)


def pageItems(request, slug):
    page = Page.objects.get(slug=slug)
    items = page.articles.all()

    context = {"items":items, "page":page}
    return render(request, "dashboard/items.html", context)


def activities(request):
    activities = Activity.objects.all()
    section = {
        "image":True,
        "activities":True
    }

    context = {"items":activities,"section":section}
    return render(request, "dashboard/items.html", context)


def productions(request):
    productions = Production.objects.all()
    section = {
        "image":True,
        "productions":True
    }

    context = {"items":productions,"section":section}
    return render(request, "dashboard/items.html", context)


def library(request):
    books = pBook.objects.all()
    section = {
        "image":False,
        "library":True
    }

    context = {"items":books, "section":section}
    return render(request, "dashboard/items.html", context)


def images(request):
    media_path = request.build_absolute_uri('/media/')
    is_ajax = request.headers.get('X-Requested-With') == 'XMLHttpRequest'

    if is_ajax:
        if request.method == 'GET':
            images = list(Image.objects.all().values())
            
            return JsonResponse({'context': images})
        return JsonResponse({'status': 'Invalid request'}, status=400)

    images = Image.objects.all()
    section = {
        "images":True
    }

    context = {"items":images,"section":section,"media_path":media_path}
    return render(request, "dashboard/files.html", context)


def audios(request):
    media_path = request.build_absolute_uri('/media/')
    is_ajax = request.headers.get('X-Requested-With') == 'XMLHttpRequest'

    if is_ajax:
        if request.method == 'GET':
            audios = list(Audio.objects.all().values())
            
            return JsonResponse({'context': audios})
        return JsonResponse({'status': 'Invalid request'}, status=400)

    audios = Audio.objects.all()
    section = {
        "audios":True
    }

    context = {"items":audios,"section":section,"media_path":media_path}
    return render(request, "dashboard/files.html", context)


def videos(request):
    is_ajax = request.headers.get('X-Requested-With') == 'XMLHttpRequest'

    if is_ajax:
        if request.method == 'GET':
            videos = list(Video.objects.all().values())
            
            return JsonResponse({'context': videos})
        return JsonResponse({'status': 'Invalid request'}, status=400)

    videos = Video.objects.all()
    section = {
        "videos":True
    }

    context = {"items":videos,"section":section}
    return render(request, "dashboard/files.html", context)


def pdfs(request):
    is_ajax = request.headers.get('X-Requested-With') == 'XMLHttpRequest'

    if is_ajax:
        if request.method == 'GET':
            pdfs = list(File.objects.all().exclude(type="doc").values())
            
            return JsonResponse({'context': pdfs})
        return JsonResponse({'status': 'Invalid request'}, status=400)

    pdfs = File.objects.all().exclude(type="doc")
    section = {
        "pdf":True
    }

    context = {"items":pdfs,"section":section}
    return render(request, "dashboard/files.html", context)

def docs(request):
    is_ajax = request.headers.get('X-Requested-With') == 'XMLHttpRequest'

    if is_ajax:
        if request.method == 'GET':
            docs = list(File.objects.all().exclude(type="pdf").values())
            
            return JsonResponse({'context': docs})
        return JsonResponse({'status': 'Invalid request'}, status=400)

    docs = File.objects.all().exclude(type="pdf")
    section = {
        "doc":True
    }

    context = {"items":docs,"section":section}
    return render(request, "dashboard/files.html", context)



# -------------------------------- Create ----------------------------
def createPage(request):
    message = ""
    if request.method == "POST":
        title = request.POST["title"]
        slug = request.POST["slug"]
        order = request.POST["order"]

        data = {"title":title,"slug":slug,"order":order}

        form = PageForm(data)
        if form.is_valid():
            form.save()
            return redirect("dashboard:dashboard")
        else:
            message = "المعلومات غير صالحة!"

    context = {"message":message}
    return render(request, "dashboard/forms/create_page.html", context)


def createItem(request, slug):
    page = Page.objects.get(slug=slug)
    message = ""

    if request.method == "POST":
        title = request.POST["title"]
        details = request.POST["details"]
        page = request.POST["page"]

        data = {"title":title, "details":details, "page":page}

        form = ArticleForm(data)

        if form.is_valid():
            form.save()
            return redirect("dashboard:page-items", slug=slug)
        else:
            message = "البيانات غير صالحة"

    context = {"message":message, "page":page}
    return render(request, "dashboard/forms/create_form.html", context)


def createActivity(request):
    media_path = request.build_absolute_uri('/media/')
    message = ""
    section = {"max":True, "image":True}

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

    context = {"section":section,"message":message,"media_path":media_path}
    return render(request, "dashboard/forms/create_form.html", context)


def createProduction(request):
    media_path = request.build_absolute_uri('/media/')
    message = ""
    section = {"book":True, "image":True}

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

    context = {"section":section,"message":message,"media_path":media_path}
    return render(request, "dashboard/forms/create_form.html", context)


def createBook(request):
    message = ""
    section = {"library":True}

    if request.method == "POST":
        title = request.POST["title"]
        author = request.POST["author"]
        translator = request.POST["translator"]
        investigator = request.POST["investigator"]
        edition = request.POST["edition"]
        pdate = request.POST["pdate"]
        description = request.POST["description"]
        century = request.POST["century"]
        language = request.POST["language"]
        phouse = request.POST["phouse"]
        size = request.POST["size"]
        crate = request.POST["crate"]
        shelf = request.POST["shelf"]

        data = {"title":title,"author":author,"translator":translator,"investigator":investigator,"edition":edition,"pdate":pdate,"description":description,"century":century,"language":language,"phouse":phouse,"size":size,"crate":crate,"shelf":shelf}

        form = PBookForm(data)

        if form.is_valid():
            form.save()
            return redirect("dashboard:library")
        else:
            message = "الرجاء ملئ جميع الحقول المطلوبة"

    context = {"section":section,"message":message}
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
        return redirect("dashboard:videos")

    context = {"options":options}
    return render(request, "dashboard/forms/upload_form.html", context)




def createAudio(request):
    options = {
        "audio":True,
        "multiple":True
    }

    if request.method == "POST":
        audio = request.FILES["audio"]
        title = request.POST["title"]

        Audio.objects.create(audio=audio,title=title)
        return redirect("dashboard:audios")

    context = {"options":options}
    return render(request, "dashboard/forms/upload_form.html", context)




# -------------------------------- Update ----------------------------
def updateItem(request, slug, pk):
    page = Page.objects.get(slug=slug)
    item = page.articles.get(id=pk)
    message = ""

    title = item.title
    details = item.details

    date = {"title":title,"details":details}

    if request.method == "POST":
        form = ArticleForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect("dashboard:page-items", slug=slug)
        else:
            message = "البيانات غير صالحة"

    context = {"page":page,"item":item, "message":message,"data":date}
    return render(request, "dashboard/forms/create_form.html", context)


def updateActivity(request, pk):
    media_path = request.build_absolute_uri('/media/')
    section = {"max":True,"image":True}
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

    context = {"section":section,"message":message,"all_images":all_images,"all_videos":all_videos,"data":data,"media_path":media_path}
    return render(request, "dashboard/forms/create_form.html", context)


def updateProduction(request, pk):
    media_path = request.build_absolute_uri('/media/')
    all_images = Image.objects.all()
    section = {"book":True}
    message = ""

    production = Production.objects.get(id=pk)
    form = ProductionForm(instance=production)
    title = production.title
    main_img = production.main_img
    body = production.body
    pdf_file = production.pdf_file
    doc_file = production.doc_file

    data = {"title":title,"main_img":main_img,"body":body,"pdf_file":pdf_file,"doc_file":doc_file}

    if request.method == "POST":
        form = ProductionForm(request.POST, instance=production)
        if form.is_valid():
            form.save()
            return redirect("dashboard:productions")
        else:
            message = "Form is not valid"

    context = {"media_path":media_path,"section":section,"message":message,"all_images":all_images,"data":data}
    return render(request, "dashboard/forms/create_form.html", context)


def updatePBook(request, pk):
    section = {"library":True}
    message = ""

    book = pBook.objects.get(id=pk)
    form = PBookForm(instance=book)
    title = book.title
    author = book.author
    translator = book.translator
    investigator = book.investigator
    edition = book.edition
    pdate = book.pdate
    description = book.description
    century = book.century
    language = book.language
    phouse = book.phouse
    size = book.size
    crate = book.crate
    shelf = book.shelf

    data = {"title":title,"author":author,"translator":translator,"investigator":investigator,"edition":edition,"pdate":pdate,"description":description,"century":century,"language":language,"phouse":phouse,"size":size,"crate":crate,"shelf":shelf}

    if request.method == "POST":
        form = PBookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect("dashboard:library")
        else:
            message = "Form is not valid"

    context = {"data":data,"section":section}
    return render(request, "dashboard/forms/create_form.html", context)



# -------------------------------- Delete ----------------------------
def deleteItem(request, slug, pk):
    page = Page.objects.get(slug=slug)
    item = page.articles.get(id=pk)

    if request.method == "POST":
        item.delete()
        return redirect("dashboard:page-items", slug=slug)
    
    context = {"item": item}
    return render(request, "dashboard/forms/delete_form.html", context)


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


def deletePBook(request, pk):
    book = pBook.objects.get(id=pk)

    if request.method == "POST":
        book.delete()
        return redirect("dashboard:library")

    context = {"item":book}
    return render(request, "dashboard/forms/delete_form.html", context)


def deleteImage(request, pk):
    if request.method == "POST":
        image = Image.objects.get(id=pk)
        if len(image.image) > 0:
            os.remove(image.image.path)
        image.delete()
        return redirect("dashboard:images")


def deleteAudio(request, pk):
    if request.method == "POST":
        audio = Audio.objects.get(id=pk)
        if len(audio.audio) > 0:
            os.remove(audio.audio.path)
        audio.delete()
        return redirect("dashboard:audios")


def deleteVideo(request, pk):
    if request.method == "POST":
        video = Video.objects.get(id=pk)
        video.delete()
        return redirect("dashboard:videos")




# -------------------------------- Activate ----------------------------
def activateActivity(request, pk):
    if request.method == "POST":
        item = Activity.objects.get(id=pk)
        if item.active == False:
            item.active = True
        elif item.active == True:
            item.active = False
        item.save()
        return redirect("dashboard:activities")


def activateProduction(request, pk):
    if request.method == "POST":
        item = Production.objects.get(id=pk)
        if item.active == False:
            item.active = True
        elif item.active == True:
            item.active = False
        item.save()
        return redirect("dashboard:productions")