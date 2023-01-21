from django.db import models


class ActivityComponents(models.Model):
    target_id = models.IntegerField()
    name = models.CharField(max_length=50, null=True)
    exported = models.BooleanField(null=True)
    permissionName = models.CharField(max_length=100, null=True)
    filterCheck = models.BooleanField()
    categoriesCheck = models.BooleanField()


class Filter(models.Model):
    comp = models.ForeignKey(
        ActivityComponents, related_name='filters', on_delete=models.CASCADE)
    name = models.CharField(max_length=50, null=True)


class Category(models.Model):
    filt = models.ForeignKey(
        Filter, related_name='categories', on_delete=models.CASCADE)
    categoryName = models.CharField(max_length=50)


class Action(models.Model):
    filt = models.ForeignKey(
        Filter, related_name='actions', on_delete=models.CASCADE)
    actionName = models.CharField(max_length=50)
