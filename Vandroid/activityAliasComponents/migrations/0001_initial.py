# Generated by Django 4.1.4 on 2023-01-20 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ActivityAliasComponents',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('target_id', models.IntegerField()),
                ('exported', models.BooleanField()),
                ('permissionName', models.CharField(max_length=50)),
            ],
        ),
    ]
