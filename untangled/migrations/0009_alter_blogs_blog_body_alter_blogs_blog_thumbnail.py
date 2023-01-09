# Generated by Django 4.1.3 on 2023-01-04 05:30

import ckeditor_uploader.fields
from django.db import migrations, models
import untangled.models


class Migration(migrations.Migration):

    dependencies = [
        ('untangled', '0008_alter_blogs_blog_userid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogs',
            name='blog_body',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='Blog Body'),
        ),
        migrations.AlterField(
            model_name='blogs',
            name='blog_thumbnail',
            field=models.ImageField(default='{% static "img/blogpost_cover" %}', upload_to=untangled.models.image_path),
        ),
    ]