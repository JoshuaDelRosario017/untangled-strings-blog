# Generated by Django 4.1.3 on 2023-02-23 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('untangled', '0009_profile_fb_url_profile_instagram_url_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogs',
            name='is_featured',
            field=models.BooleanField(default=False),
        ),
    ]
