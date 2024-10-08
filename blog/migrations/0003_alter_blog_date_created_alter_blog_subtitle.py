# Generated by Django 5.0.7 on 2024-08-20 17:17

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20240820_1337'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='date_created',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='blog',
            name='subtitle',
            field=models.CharField(blank=True, max_length=800, null=True),
        ),
    ]
