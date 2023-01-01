from django.db import models

class Permission(models.Model):
    Uses_Name = models.CharField()
    Uses_Status = models.CharField(max_length=17)
    Uses_Info = models.CharField()
    Uses_Description = models.CharField()

    Custom_Name = models.CharField()
    Custom_Status = models.CharField(max_length=17)
    Custom_Info = models.CharField()
    Custom_Description = models.CharField()

    API_Name = models.CharField()
    API_Status = models.CharField(max_length=17)
    API_Info = models.CharField()
