from django.urls import path
from . import views

app_name = "backend"

urlpatterns = [
    path("", views.home, name="home"),

    path("activities/", views.activities, name="activities"),
    path("activity/<str:pk>", views.activity, name="activity")
]