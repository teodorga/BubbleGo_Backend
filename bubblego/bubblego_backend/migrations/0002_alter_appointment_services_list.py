# Generated by Django 3.2.4 on 2023-06-23 09:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bubblego_backend', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='services_list',
            field=models.ManyToManyField(to='bubblego_backend.Service'),
        ),
    ]