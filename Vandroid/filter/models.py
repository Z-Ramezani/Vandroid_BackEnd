from django.db import models


class Filter(models.Model):

    target_id = models.IntegerField()
    target_id_comp = models.IntegerField()
    componentName = models.CharField(max_length=20)
    name = models.CharField(max_length=50)
    # FilterCategory = models.CharField(max_length=50)
    # FilterAction = models.CharField(max_length=50)
