from django.db import models


class APIPermission(models.Model):
    target_id = models.IntegerField()
    name = models.CharField(max_length=50)
    status = models.CharField(max_length=17)
    info = models.CharField(max_length=100)
