# Generated by Django 5.1.3 on 2024-12-01 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nutriwise', '0004_remove_userprofile_bio_remove_userprofile_food_image_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='food_image',
            field=models.ImageField(blank=True, null=True, upload_to='food_images/'),
        ),
    ]
