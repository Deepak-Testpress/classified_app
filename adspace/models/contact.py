from django.core.validators import RegexValidator
from django.db import models
from model_utils.models import TimeStampedModel


class Contact(TimeStampedModel):
    email = models.EmailField()
    phone_number = models.CharField(
        max_length=10,
        validators=[RegexValidator(r"^[6-9]\d{9}$", ("Invalid Phone number"))],
    )
