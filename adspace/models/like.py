from django.contrib.auth.models import User
from django.db import models
from model_utils.models import TimeStampedModel

from .post import Post


class Like(TimeStampedModel):
    pass
    liked_by = models.ManyToManyField(User, related_name="liked_by")
    liked_post = models.ManyToManyField(Post, related_name="liked_posts")
