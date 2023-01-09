from django.urls import path
from . import views

app_name = "dashboard"

urlpatterns = [
    # Display
    path("", views.index, name="dashboard"),

    path("activities/", views.activities, name="activities"),

    path("productions/", views.productions, name="productions"),

    path("images/", views.images, name="images"),


    # Create
    path("create-activity/", views.createActivity, name="create-activity"),

    path("create-production/", views.createProduction, name="create-production"),

    path("upload-image/", views.createImage, name="create-image"),

    path("add-video/", views.createVideo, name="create-video"),
    
    path("upload-audio/", views.createAudio, name="create-audio"),


    # Update
    path("update-activity/<str:pk>/", views.updateActivity, name="update-activity"),

    path("update-production/<str:pk>/", views.updateProduction, name="update-production"),
    
    
    # Delete
    path("delete-activity/<str:pk>/", views.deleteActivity, name="delete-activity"),

    path("delete-production/<str:pk>/", views.deleteProduction, name="delete-production"),
    
    path("delete-image/<str:pk>/", views.deleteImage, name="delete-image")
]