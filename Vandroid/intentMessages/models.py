from django.db import models

# Create your models here.


class IntentMessages(models.Model):
    target_id = models.IntegerField()
    name = models.CharField(max_length=100, null=True)
    type = models.CharField(max_length=8, null=True)
    permission = models.CharField(max_length=100, null=True)
    senderComponent = models.CharField(max_length=100, null=True)
    targetComponent = models.CharField(max_length=100, null=True)
