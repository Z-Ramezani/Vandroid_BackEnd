from django.db import models


class ActivityComponents(models.Model):
    target_id = models.IntegerField()
    Exported = models.BooleanField()
    # FilterName = models.CharField(max_length=50)
    # FilterCategory = models.CharField(max_length=50)
    # FilterAction = models.CharField(max_length=50)
    PermissionName = models.CharField(max_length=50)
