from .models import Page

def pages(request):
    pages = Page.objects.order_by("order")
    return {'pages': pages}