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
            "img_array": "تحديد صور"
        }

class ImageForm(ModelForm):
    class Meta:
        model = Image
        fields = "__all__"
        labels = {
            "image": "رفع صور "
        }