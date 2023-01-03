from django.db import models


class UsesPermission(models.Model):
    target_id = models.IntegerField()
    name = models.CharField(max_length=50)
    status = models.CharField(max_length=30)
    info = models.CharField(max_length=250)
    description = models.CharField(max_length=250)
