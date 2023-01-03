from django.db import models

# Create your models here.


class IntentMessages(models.Model):
    target_id = models.IntegerField()
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=8)
    Permission = models.CharField(max_length=100)
    senderComponent = models.CharField(max_length=100)
    targetComponent = models.CharField(max_length=100)
