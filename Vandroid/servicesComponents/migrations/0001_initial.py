# Generated by Django 4.1.4 on 2023-01-25 10:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ServicesComponents',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('target_id', models.IntegerField()),
                ('name', models.CharField(max_length=50, null=True)),
                ('exported', models.BooleanField(null=True)),
                ('permissionName', models.CharField(max_length=100, null=True)),
                ('filterCheck', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Filter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, null=True)),
                ('categoriesCheck', models.BooleanField()),
                ('comp', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='filters', to='servicesComponents.servicescomponents')),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categoryName', models.CharField(max_length=50, null=True)),
                ('filt', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='categories', to='servicesComponents.filter')),
            ],
        ),
        migrations.CreateModel(
            name='Action',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('actionName', models.CharField(max_length=50, null=True)),
                ('filt', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='actions', to='servicesComponents.filter')),
            ],
        ),
    ]
