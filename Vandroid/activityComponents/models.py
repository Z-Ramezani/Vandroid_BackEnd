from django.db import models


class ActivityComponents(models.Model):
    target_id = models.IntegerField()
    exported = models.BooleanField()
    permissionName = models.CharField(max_length=50)

class Filter(models.Model):
    comp = models.ForeignKey(ActivityComponents, related_name='filters', on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    def __unicode__(self):
        return self.name
    # FilterCategory = models.CharField(max_length=50)
    # FilterAction = models.CharField(max_length=50)
