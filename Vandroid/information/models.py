from django.db import models


class Information(models.Model):
    nameApp = models.CharField(max_length=100)
    file_name = models.CharField(max_length=100, null=True)
    file_size = models.IntegerField(null=True)
    # file_MD5 = models.CharField(max_length=250)
    # file_sha256 = models.CharField(max_length=250)
    app_name = models.CharField(max_length=100, null=True)
    app_package = models.CharField(max_length=100, null=True)
    app_lable = models.CharField(max_length=100, null=True)
    app_icon = models.CharField(max_length=100, null=True)
    app_MinSDKVersion = models.CharField(max_length=5, null=True)
    app_MaxSDKVersion = models.CharField(max_length=5, null=True)
    app_TargetSDKVersion = models.CharField(max_length=5, null=True)
    app_AndroidVersionCode = models.CharField(max_length=5, null=True)
    app_AndroidVersionName = models.CharField(max_length=5, null=True)
