from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE

# Create your models here.
class Money(models.Model):
    user = models.ForeignKey(User, on_delete=CASCADE, null=True)
    price = models.CharField(max_length=1000000)

class VerificationBadge(models.Model):
    user = models.ForeignKey(User, on_delete=CASCADE, null=True)