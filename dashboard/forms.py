from django.forms import ModelForm
from backend.models import *


class PageForm(ModelForm):
    class Meta:
        model = Page
        fields = "__all__"

class ArticleForm(ModelForm):
    class Meta:
        model = Article
        fields = "__all__"

class ActivityForm(ModelForm):
    class Meta:
        model = Activity
        fields = "__all__"


class ProductionForm(ModelForm):
    class Meta:
        model = Production
        fields = "__all__"


class PBookForm(ModelForm):
    class Meta:
        model = pBook
        fields = "__all__"

class ImageForm(ModelForm):
    class Meta:
        model = Image
        fields = "__all__"
        labels = {
            "image": "رفع صور ",
            "title": "العنوان"
        }