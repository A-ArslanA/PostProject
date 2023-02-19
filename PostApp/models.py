from django.db import models
from datetime import datetime

class Post(models.Model):
    title = models.CharField("Title", max_length=255)
    postDate = models.DateTimeField("Published date", default=datetime.now)
    image = models.CharField("Image", max_length=500, blank=True, null=True)
    content = models.TextField("Content")

    def __str__(self):
        return f"{self.title} - {self.postDate}"

