from django.urls import path
from . import views

urlpatterns = [
    # Display
    path("activities/", views.activities, name="activities"),
    path("images/", views.images, name="images"),


    # Create
    path("create-activity/", views.createActivity, name="create-activity"),
    path("upload-image/", views.createImage, name="create-image"),


    # Update
    path("update-activity/<str:pk>/", views.updateActivity, name="update-activity"),
]