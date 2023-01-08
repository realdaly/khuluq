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
        return f"{self.id}- {self.title} ({self.audio.path})"




class Video(models.Model):
    vid_id = models.CharField(max_length=5000, blank=False)
    title = models.CharField(max_length=1000, blank=False)

    def __str__(self):
        return f"{self.title}"




class File(models.Model):
    file = models.FileField(upload_to="files", blank=False)
    title = models.CharField(max_length=1000, blank=True)

    def __str__(self):
        return f"{self.title}({self.file.path})"




class Activity(models.Model):
    title = models.CharField(max_length=1000, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    main_img = models.ForeignKey(Image, on_delete=models.PROTECT, blank=False)
    body = models.TextField(max_length=5000, blank=False)
    img_array = models.ManyToManyField(Image, blank=True, related_name="images")
    vid_array = models.ManyToManyField(Video, blank=True, related_name="videos")
    audio = models.CharField(max_length=1000, blank=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title




class Production(models.Model):
    title = models.CharField(max_length=1000, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    main_img = models.ForeignKey(Image, on_delete=models.PROTECT, blank=False)
    body = models.TextField(max_length=5000, blank=False)
    pdf_file = models.CharField(max_length=1000, blank=True)
    doc_file = models.CharField(max_length=1000, blank=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title