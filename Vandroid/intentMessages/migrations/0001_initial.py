# Generated by Django 4.1.4 on 2023-01-01 08:15

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
                ('name', models.CharField(max_length=20)),
                ('type', models.CharField(max_length=8)),
                ('Permission', models.CharField(max_length=20)),
                ('senderComponent', models.CharField(max_length=50)),
                ('targetComponent', models.CharField(max_length=50)),
            ],
        ),
    ]
