# Generated by Django 4.1.4 on 2023-01-21 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('broadcastReceiversComponents', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='broadcastreceiverscomponents',
            name='permissionName',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
