from django.db import models
from model_utils.models import TimeStampedModel


class Category(TimeStampedModel):
    name = models.CharField(max_length=256, db_index=True)
    slug = models.CharField(
        max_length=256, db_index=True, blank=True, unique=True
    )
