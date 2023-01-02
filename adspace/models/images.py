from django.db import models
from model_utils.models import TimeStampedModel

from .post import Post


class Image(TimeStampedModel):
    title = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True, blank=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    url = models.URLField()
    image = models.ImageField(upload_to="images/%Y/%m/%d/")
