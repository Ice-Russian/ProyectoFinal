# Generated by Django 5.0.7 on 2024-08-15 06:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_userprofile_first_name_userprofile_last_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='profile_image',
            field=models.ImageField(blank=True, null=True, upload_to='media/profile_images/'),
        ),
    ]
