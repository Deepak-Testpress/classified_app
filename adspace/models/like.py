from django.contrib.auth.models import User
from django.db import models
from model_utils.models import TimeStampedModel

from .post import Post


class Like(TimeStampedModel):
    liked_by = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="liked_by"
    )
    liked_post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name="liked_posts"
    )
