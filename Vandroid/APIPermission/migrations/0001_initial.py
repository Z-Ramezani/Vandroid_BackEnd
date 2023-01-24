# Generated by Django 4.1.4 on 2023-01-24 09:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='APIPermission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('target_id', models.IntegerField()),
                ('name', models.CharField(max_length=100)),
                ('status', models.CharField(max_length=30)),
                ('info', models.CharField(max_length=250)),
            ],
        ),
    ]
