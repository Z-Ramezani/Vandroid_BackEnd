from unicodedata import name
from django.db import models


class components(models.Model):


    

    BroadcastReceivers_Exported = models.BooleanField()
    BroadcastReceivers_FilterName = models.CharField()
    BroadcastReceivers_FilterCategory = models.CharField()
    BroadcastReceivers_FilterAction = models.CharField()
    BroadcastReceivers_PermissionName = models.CharField()

    ContentProviders_Exported = models.BooleanField()
    ContentProviders_Authority = models.CharField()
    ContentProviders_PermissionName = models.CharField()

    DynamicRegistered_Exported = models.BooleanField()
    DynamicRegistered_FilterName = models.CharField()
    DynamicRegistered_FilterCategory = models.CharField()
    DynamicRegistered_FilterAction = models.CharField()
    DynamicRegistered_PermissionName = models.CharField()