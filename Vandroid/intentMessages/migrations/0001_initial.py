# Generated by Django 4.1.4 on 2023-01-20 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='IntentMessages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('target_id', models.IntegerField()),
                ('name', models.CharField(max_length=100)),
                ('type', models.CharField(max_length=8)),
                ('permission', models.CharField(max_length=100)),
                ('senderComponent', models.CharField(max_length=100)),
                ('targetComponent', models.CharField(max_length=100)),
            ],
        ),
    ]
