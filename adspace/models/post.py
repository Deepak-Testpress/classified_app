from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from django.db import models
from model_utils.models import TimeStampedModel
from taggit.managers import TaggableManager

from .category import Category
from .contact import Contact


class Post(TimeStampedModel):
    TYPES = (
        ("job", "Job"),
        ("gig", "Gig"),
        ("for sale", "For sale"),
        ("service", "Service"),
        ("event", "Event"),
        ("class", "Class"),
    )
    title = models.CharField(max_length=256)
    slug = models.TextField(max_length=256, blank=True, unique=True)
    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    tags = TaggableManager(blank=True)
    postal_code = models.CharField(
        max_length=6,
        validators=[RegexValidator("^[0-9]{6}$", ("Invalid postal code"))],
    )
    location = models.CharField(max_length=200)
    description = models.TextField(max_length=256)
    contact_info = models.OneToOneField(Contact, on_delete=models.CASCADE)
    show_contact_info = models.BooleanField(default=True)
    price = models.IntegerField()
    date = models.DateTimeField(blank=True, null=True)
    type = models.CharField(max_length=12, choices=TYPES)
    category = models.ForeignKey(
        Category, on_delete=models.DO_NOTHING, related_name="posts"
    )
