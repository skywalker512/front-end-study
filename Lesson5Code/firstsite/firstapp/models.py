from django.db import models


# Create your models here.


class Ariticle(models.Model):
    headline = models.CharField(null=True, blank=True, max_length=500)
    content = models.TextField(null=True, blank=True)
    TAG_CHOICES = (
        ('tech', 'Tech'),
        ('life', 'Life'),
    )
    tag = models.CharField(
        null=True,
        blank=True,
        max_length=5,
        choices=TAG_CHOICES
    )

    def __str__(self):
        return self.headline


class Comment(models.Model):
    name = models.CharField(null=True, blank=True, max_length=200)
    comment = models.TextField(null=True, blank=True)
    belong_to = models.ForeignKey(
        to=Ariticle,
        related_name='under_comments',
        on_delete=models.CASCADE,
        null=True,
        blank=True)
    best_comment = models.BooleanField(default=False)

    def __str__(self):
        return self.comment
