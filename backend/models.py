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



type_list= ['pdf','doc']
class File(models.Model):
    FILE_CHOICES=sorted([(item, item) for item in type_list])

    file = models.FileField(upload_to="files", blank=False)
    title = models.CharField(max_length=1000, blank=True)
    type = models.CharField(max_length=10, choices=FILE_CHOICES, blank=True)

    def __str__(self):
        return f"{self.title}({self.file.path})"




class Activity(models.Model):
    title = models.CharField(max_length=1000, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    main_img = models.ForeignKey(Image, on_delete=models.PROTECT, blank=False)
    body = models.TextField(max_length=5000, blank=False)
    img_array = models.ManyToManyField(Image, blank=True, related_name="images")
    vid_array = models.ManyToManyField(Video, blank=True, related_name="videos")
    audio = models.ForeignKey(Audio, on_delete=models.PROTECT, blank=True, null=True)
    active = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title




class Production(models.Model):
    title = models.CharField(max_length=1000, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    main_img = models.ForeignKey(Image, on_delete=models.PROTECT, blank=False)
    body = models.TextField(max_length=5000, blank=False)
    pdf_file = models.ForeignKey(File, on_delete=models.PROTECT, blank=True, null=True, related_name="pdf")
    doc_file = models.ForeignKey(File, on_delete=models.PROTECT, blank=True, null=True, related_name="doc")
    active = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title




class pBook(models.Model):
    title = models.CharField(max_length=1000, blank=True)
    author = models.CharField(max_length=1000, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.title} - {self.author}"