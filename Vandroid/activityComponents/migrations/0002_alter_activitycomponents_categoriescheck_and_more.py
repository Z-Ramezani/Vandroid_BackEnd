# Generated by Django 4.1.4 on 2023-01-21 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activityComponents', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activitycomponents',
            name='categoriesCheck',
            field=models.BooleanField(),
        ),
        migrations.AlterField(
            model_name='activitycomponents',
            name='filterCheck',
            field=models.BooleanField(),
        ),
    ]