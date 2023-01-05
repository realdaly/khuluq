from django.urls import path
from . import views

app_name = "dashboard"

urlpatterns = [
    # Display
    path("", views.index, name="dashboard"),

    path("activities/", views.activities, name="activities"),

    path("images/", views.images, name="images"),


    # Create
    path("create-activity/", views.createActivity, name="create-activity"),

    path("upload-image/", views.createImage, name="create-image"),

    path("add-video/", views.createVideo, name="create-video"),
    
    path("upload-audio/", views.createAudio, name="create-audio"),


    # Update
    path("update-activity/<str:pk>/", views.updateActivity, name="update-activity"),
    
    
    # Delete
    path("delete-activity/<str:pk>/", views.deleteActivity, name="delete-activity")
]