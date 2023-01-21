from django.db import models


class ContentProvidersComponents(models.Model):
    target_id = models.IntegerField()
    name = models.CharField(max_length=50, null=True)
    exported = models.BooleanField(null=True)
    permissionName = models.CharField(max_length=100, null=True)
    Authority = models.CharField(max_length=100, null=True)