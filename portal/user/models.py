from django.db import models
from django.contrib.auth.models import User
import uuid


# Create your models here.
class UserExt(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    activation_link = models.UUIDField(default=uuid.uuid4)
    activated = models.BooleanField()
