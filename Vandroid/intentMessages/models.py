from django.db import models

# Create your models here.

class IntentMessages(models.Model):
    name = models.CharField(max_length=20)
    type = models.CharField(max_length=8)
    Permission = models.CharField(max_length=20)
    senderComponent = models.CharField(max_length=50)
    targetComponent = models.CharField(max_length=50)
