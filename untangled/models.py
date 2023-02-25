from django.db import models
from ckeditor.fields import RichTextField
from datetime import datetime
import uuid
from django.utils import timezone
import os, random
from django.contrib.auth.models import User
from ckeditor_uploader.fields import RichTextUploadingField
import json
# from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# Create your models here.

now = timezone.now()

def image_path(instance, filename):
    basefilename, file_extension = os.path.splitext(filename)
    chars='ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890'
    randomstr = ''.join((random.choice(chars)) for x in range(10))
    _now = datetime.now()

    return 'profile_pics/{year}-{month}-{imageid}-{basename}-{randomstring}{ext}'.format(imageid=instance, basename=basefilename, randomstring=randomstr, ext=file_extension, year=_now.strftime('%y'), month=_now.strftime('%m'), day=_now.strftime('%d'))

class Blogs(models.Model):
    blog_id = models.AutoField(primary_key=True, unique=True,editable=False)
    blog_thumbnail = models.ImageField(upload_to=image_path, default='/media/blogpost_cover.jpg')
    blog_title = models.CharField(max_length=200, verbose_name ='Blog Title')
    blog_description = models.TextField(max_length=255, default='', verbose_name='Blog Description')
    blog_body = RichTextUploadingField(blank=True, null=True, verbose_name='Blog Body')
    blog_pubdate = models.DateTimeField(null=True)
    blog_author = models.CharField(max_length=100,verbose_name='Blog Author', default=False)
    blog_user = models.ForeignKey(User,  on_delete=models.CASCADE)
    blog_category = models.CharField(max_length=255, verbose_name='Blog Category')
    # blog_tags = models.JSONField(null=True, verbose_name='Tags')
    deleted_on = models.DateTimeField(verbose_name='Deleted Date-Time', null=True)
    is_draft = models.BooleanField(null=False, default=False)
    likes = models.ManyToManyField(User, related_name='blog_id')
    is_featured = models.BooleanField(null=False, default=False)

    class Meta:
        ordering = ['blog_id']
        
    def total_likes(self):
        return self.likes.count()
    
    def __str__(self):
        return self.blog_title

    # def get_blog_tags(self):
    #     return json.loads(self.blog_tags)


# class tags(models.Model):
#     blog_id = models.ForeignKey(Blogs, related_name='blog_tags', on_delete=models.CASCADE)
#     blog_tags = models.CharField(max_length=100, verbose_name='Blog Category')

class Category(models.Model):
    blog_categories = models.CharField(max_length=50, verbose_name='category')

    class Meta:
        ordering = ['id']

    def __str__(self):
        return self.blog_categories

class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    bio = models.TextField()
    profile_pic = models.ImageField(null=True, blank=True, upload_to=image_path)
    website_url = models.CharField(max_length=255, null=True, blank=True)
    fb_url = models.CharField(max_length=255, null=True, blank=True)
    twitter_url = models.CharField(max_length=255, null=True, blank=True)
    instagram_url = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return str(self.user)


