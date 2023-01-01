from django.db import models

class UsesPermission(models.Model):
    name = models.CharField(max_length=50)
    status = models.CharField(max_length=17)
    info = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
