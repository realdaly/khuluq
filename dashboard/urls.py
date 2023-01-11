from django.urls import path
from . import views

app_name = "dashboard"

urlpatterns = [
    # Display
    path("", views.index, name="dashboard"),

    path("activities/", views.activities, name="activities"),

    path("productions/", views.productions, name="productions"),

    path("images/", views.images, name="images"),

    path("audios/", views.audios, name="audios"),

    path("videos/", views.videos, name="videos"),


    # Create
    path("create-activity/", views.createActivity, name="create-activity"),

    path("create-production/", views.createProduction, name="create-production"),

    path("upload-image/", views.createImage, name="create-image"),

    path("add-video/", views.createVideo, name="create-video"),
    
    path("upload-audio/", views.createAudio, name="create-audio"),


    # Update
    path("update-activity/<str:pk>/", views.updateActivity, name="update-activity"),
    path("activate-activity/<str:pk>/ ", views.activateActivity, name="activate-activity"),

    path("update-production/<str:pk>/", views.updateProduction, name="update-production"),
    path("activate-production/<str:pk>/ ", views.activateProduction, name="activate-production"),
    
    
    # Delete
    path("delete-activity/<str:pk>/", views.deleteActivity, name="delete-activity"),

    path("delete-production/<str:pk>/", views.deleteProduction, name="delete-production"),
    
    path("delete-image/<str:pk>/", views.deleteImage, name="delete-image"),

    path("delete-audio/<str:pk>/", views.deleteAudio, name="delete-audio"),
    
    path("delete-video/<str:pk>/", views.deleteVideo, name="delete-video")
]