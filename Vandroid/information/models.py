from django.db import models


class Information(models.Model):
    nameApp = models.CharField(max_length=250)
    name = models.CharField(max_length=250)
    size = models.IntegerField()
    # file_MD5 = models.CharField(max_length=250)
    # file_sha256 = models.CharField(max_length=250)
    app_name = models.CharField(max_length=50)
    app_package = models.CharField(max_length=50)
    app_lable = models.CharField(max_length=50)
    app_icon = models.CharField(max_length=50)
    app_MinSDKVersion = models.CharField(max_length=5)
    app_MaxSDKVersion = models.CharField(max_length=5)
    app_TargetSDKVersion = models.CharField(max_length=5)
    app_AndroidVersionCode = models.CharField(max_length=5)
    app_AndroidVersionName = models.CharField(max_length=5)
