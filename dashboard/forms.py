from django.forms import ModelForm
from backend.models import *

class ActivityForm(ModelForm):
    class Meta:
        model = Activity
        fields = "__all__"
        labels = {
            "title": "العنوان",
            "main_img": "الصورة الرئيسية",
            "body": "نص المقال",
        }

class ImageForm(ModelForm):
    class Meta:
        model = Image
        fields = "__all__"