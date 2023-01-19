from django.db import models


class ActivityAliasComponents(models.Model):

    target_id = models.IntegerField()
    exported = models.BooleanField()
    permissionName = models.CharField(max_length=50)
