from django.db import models


# Create your models here.
class Video(models.Model):
    title = models.CharField(null=True, blank=True, max_length=300)
    conten = models.TextField(null=True, blank=True)
    url_image = models.URLField(null=True, blank=True)
    editors_choice = models.BooleanField(null=True, blank=True)

    def __str__(self):
        return self.title
