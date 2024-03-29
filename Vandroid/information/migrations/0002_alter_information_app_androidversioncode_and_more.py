# Generated by Django 4.1.4 on 2023-01-25 06:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('information', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='information',
            name='app_AndroidVersionCode',
            field=models.CharField(max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='information',
            name='app_AndroidVersionName',
            field=models.CharField(max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='information',
            name='app_MaxSDKVersion',
            field=models.CharField(max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='information',
            name='app_MinSDKVersion',
            field=models.CharField(max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='information',
            name='app_TargetSDKVersion',
            field=models.CharField(max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='information',
            name='app_icon',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='information',
            name='app_lable',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='information',
            name='app_name',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='information',
            name='app_package',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='information',
            name='file_name',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='information',
            name='file_size',
            field=models.IntegerField(null=True),
        ),
    ]
