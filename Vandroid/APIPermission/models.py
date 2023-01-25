from django.db import models


class APIPermission(models.Model):
    target_id = models.IntegerField()
    name = models.CharField(max_length=100, null=True)
    status = models.CharField(max_length=30, null=True)
    info = models.CharField(max_length=250, null=True)
