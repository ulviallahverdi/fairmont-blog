from django.db import models

class Video(models.Model):
    name = models.CharField(max_length=200)
    url = models.FileField(verbose_name="video_url",upload_to='static/')