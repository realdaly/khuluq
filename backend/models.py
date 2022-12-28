from django.db import models

from django.utils.html import mark_safe

# Create your models here.
class Image(models.Model):
    image = models.ImageField(upload_to='images', blank=True)




class Activity(models.Model):
    title = models.CharField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)
    main_img = models.CharField(max_length=1000, blank=False)
    body = models.TextField(max_length=5000)
    img_array = models.ManyToManyField(Image, blank=True, related_name="activities")

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title