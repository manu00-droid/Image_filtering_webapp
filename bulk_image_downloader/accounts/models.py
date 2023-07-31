from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class custom_user(AbstractUser):
    current_plan = models.CharField(max_length=100, default='free')
    current_plan_expiry = models.DateTimeField(null=True, blank=True)
    is_subscribed = models.BooleanField(default=False)
