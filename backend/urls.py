from django.urls import path
from . import views

app_name = "backend"

urlpatterns = [
    path("", views.home, name="home"),

    path("<str:slug>/", views.page_items, name="items"),

    path("<str:slug>/<str:pk>", views.item_details, name="itemDetails"),

    path("activities/", views.activities, name="activities"),
    path("activity/<str:pk>/", views.activity, name="activity"),

    path("productions", views.productions, name="productions"),
    path("production/<str:pk>/", views.production, name="production"),

    path("library/", views.pBooks, name="library"),
    path("searchLibrary/", views.searchLibrary, name="searchLibrary"),

]