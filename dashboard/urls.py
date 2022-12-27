from django.urls import path
from . import views

urlpatterns = [
    path("activities/", views.activities, name="activities"),
    path("create-activity/", views.createActivity, name="create-activity"),
    path("update-activity/<str:pk>/", views.updateActivity, name="update-activity"),
]