from django.db import models

# Create your models here.
class Image(models.Model):
    image = models.ImageField(upload_to="images", blank=False)

    def __str__(self):
        return f"{self.id}"




class Audio(models.Model):
    audio = models.FileField(upload_to="audio", blank=False)
    title = models.CharField(max_length=1000, blank=True)

    def __str__(self):
        return f"{self.id}- {self.title}"




class Video(models.Model):
    vid_id = models.CharField(max_length=5000)
    title = models.CharField(max_length=1000)

    def __str__(self):
        return f"{self.title}"




class Activity(models.Model):
    title = models.CharField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)
    main_img = models.ForeignKey(Image, on_delete=models.PROTECT, related_name="mainImage")
    body = models.TextField(max_length=5000)
    img_array = models.ManyToManyField(Image, blank=True, related_name="images")
    vid_array = models.ManyToManyField(Video, blank=True, related_name="videos")
    audio = models.CharField(max_length=1000, blank=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title