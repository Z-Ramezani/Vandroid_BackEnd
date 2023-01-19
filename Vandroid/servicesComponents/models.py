from django.db import models


class ServicesComponents(models.Model):
    target_id = models.IntegerField()
    Exported = models.BooleanField()
    # FilterName = models.CharField()
    # FilterCategory = models.CharField()
    # FilterAction = models.CharField()
    PermissionName = models.CharField(max_length=50)
