# Generated by Django 4.1.4 on 2023-01-25 06:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activityComponents', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='action',
            name='actionName',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='category',
            name='categoryName',
            field=models.CharField(max_length=50, null=True),
        ),
    ]